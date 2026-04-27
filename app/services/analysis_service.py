from sqlalchemy.orm import Session
from app.models.analysis import Analysis
from app.analyzer import analyze_text
import logging

logger = logging.getLogger(__name__)


def create_analysis(db: Session, title: str, content: str):
    """
    Create a new text analysis, persist it, and return structured results.
    """
    try:
        results = analyze_text(content)

        analysis = Analysis(
            title=title,
            content=content,
            word_count=results["word_count"],
            char_count=results["char_count"],
            reading_time_minutes=results["reading_time_minutes"],
        )

        db.add(analysis)
        db.commit()
        db.refresh(analysis)

        return {
            "id": analysis.id,
            "title": analysis.title,
            "content": analysis.content,
            **results,
        }

    except Exception as e:
        logger.error(f"Error creating analysis: {e}")
        db.rollback()
        raise


def update_analysis(db: Session, analysis_id: int, update_data: dict):
    """Update an analysis. Recompute metrics if content changes."""
    try:
        analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()

        if not analysis:
            return None

        for key, value in update_data.items():
            setattr(analysis, key, value)

        # keep metrics consistent if content is updated
        if "content" in update_data:
            results = analyze_text(update_data["content"])

            analysis.word_count = results["word_count"]
            analysis.char_count = results["char_count"]
            analysis.reading_time_minutes = results["reading_time_minutes"]

        db.commit()
        db.refresh(analysis)

        return analysis

    except Exception as e:
        logger.error(f"Error updating analysis {analysis_id}: {e}")
        db.rollback()
        raise


def delete_analysis(db: Session, analysis_id: int):
    """Delete an analysis by ID."""
    try:
        analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()

        if not analysis:
            return None

        db.delete(analysis)
        db.commit()
        return True

    except Exception as e:
        logger.error(f"Error updating analysis {analysis_id}: {e}")
        db.rollback()
        raise


def get_analysis(db: Session, analysis_id: int):
    """Return a single analysis by ID."""
    return db.query(Analysis).filter(Analysis.id == analysis_id).first()


def get_all_analyses(db: Session):
    """Return all analyses."""
    return db.query(Analysis).all()
