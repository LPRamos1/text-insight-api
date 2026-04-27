import re
from collections import Counter
from pydantic import BaseModel
from typing import Dict


def analyze_text(text: str):
    """
    Analyze a text and return basic metrics such as word count,
    character count, reading time, and top keywords.

    Business rules:
    - Reading time is estimated using 200 words per minute
    - Keywords ignore words shorter than 4 characters
    """

    char_count = len(text)
    words = re.findall(r"\b\w+(?:[-']\w+)*\b", text.lower())
    word_count = len(words)

    # Estimate reading time based on average speed (200 words/minute)
    reading_time = round(word_count / 200, 2)
    if reading_time < 0.01:
        reading_time = 0.01

    # Ignore short words to improve keyword relevance
    filtered_words = [w for w in words if len(w) > 3]
    top_keywords = dict(Counter(filtered_words).most_common(5))

    return {
        "word_count": word_count,
        "char_count": char_count,
        "reading_time_minutes": reading_time,
        "top_keywords": top_keywords,
    }
