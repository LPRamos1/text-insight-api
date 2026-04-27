from pydantic import BaseModel, Field
from typing import Dict, Optional


class TextInput(BaseModel):
    """Schema for creating a new text analysis."""

    title: str = Field(
        ...,
        json_schema_extra={"example": "Just a Text"},
        description="The title of the text",
    )
    content: str = Field(
        default=...,
        min_length=10,
        json_schema_extra={
            "example": "This is an example of a long text for analyzes."
        },
        description="The main content to be processed",
    )


class TextUpdate(BaseModel):
    """Schema for updating an existing analysis."""

    title: Optional[str] = None
    content: Optional[str] = None


class TextAnalysisResponse(BaseModel):
    """Schema returned after processing a text analysis."""

    id: int
    title: str
    content: str
    word_count: int
    char_count: int
    reading_time_minutes: float
    top_keywords: Dict[str, int]
