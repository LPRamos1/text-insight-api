import re
from collections import Counter


def analyze_text(text: str):
    """
    Analyzes the provided text and calculates key metrics.

    Args:
        text (str): The raw string content to be analyzed.

    Returns:
        Dict[str, Any]: A dictionary containing word count, character count,
                        estimated reading time, and top keywords.
    """
    char_count = len(text)
    words = re.findall(r"\w+", text.lower())
    word_count = len(words)

    # Average reading speed: 200 words per minute
    reading_time = round(word_count / 200, 2)
    if reading_time < 0.01:
        reading_time = 0.01

    # Filter short words (less than 4 chars) to find meaningful keywords
    filtered_words = [w for w in words if len(w) > 3]
    top_keywords = dict(Counter(filtered_words).most_common(5))

    return {
        "word_count": word_count,
        "char_count": char_count,
        "reading_time_minutes": reading_time,
        "top_keywords": top_keywords,
    }
