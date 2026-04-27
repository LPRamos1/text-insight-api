from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.analysis import TextInput, TextUpdate, TextAnalysisResponse
from app.services import analysis_service

from app.models.analysis import Analysis
from app.analyzer import analyze_text


router = APIRouter()


@router.post("/")
def create(data: TextInput, db: Session = Depends(get_db)):
    """Create a new text analysis."""
    return analysis_service.create_analysis(db, data.title, data.content)


@router.get("/health")
def test_db(db: Session = Depends(get_db)):
    """Health check endpoint."""
    return {"status": "connected"}


@router.get("/", response_model=list[TextAnalysisResponse])
def list_all(db: Session = Depends(get_db)):
    """Return all analyses."""
    analyses = analysis_service.get_all_analyses(db)

    result = []
    for analysis in analyses:
        results = analyze_text(analysis.content)

        result.append(
            {
                "id": analysis.id,
                "title": analysis.title,
                "content": analysis.content,
                **results,
            }
        )

    return result


@router.get("/{analysis_id}", response_model=TextAnalysisResponse)
def get_by_id(analysis_id: int, db: Session = Depends(get_db)):
    """Return a single analysis by ID."""
    analysis = analysis_service.get_analysis(db, analysis_id)

    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")

    results = analyze_text(analysis.content)

    return {
        "id": analysis.id,
        "title": analysis.title,
        "content": analysis.content,
        **results,
    }


@router.put("/{analysis_id}")
def update(analysis_id: int, data: TextUpdate, db: Session = Depends(get_db)):
    """Update an existing analysis."""
    update_data = data.dict(exclude_unset=True, exclude_none=True)
    analysis = analysis_service.update_analysis(db, analysis_id, update_data)

    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return {"message": "Updated successfully"}


@router.delete("/{analysis_id}")
def delete(analysis_id: int, db: Session = Depends(get_db)):
    """Delete an analysis by ID."""
    success = analysis_service.delete_analysis(db, analysis_id)

    if not success:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return {"message": "Deleted successfully"}
