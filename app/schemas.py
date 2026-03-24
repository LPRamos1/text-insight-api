from pydantic import BaseModel, Field
from typing import Dict


#
class TextInput(BaseModel):
    #
    title: str = Field(
        default=...,
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


#
class TextAnalysisResponse(BaseModel):
    word_count: int
    char_count: int
    reading_time_minutes: float
    # Dict where key is the word str and the value is int
    top_keywords: Dict[str, int]
