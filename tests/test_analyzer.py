import pytest
from app.analyzer import analyze_text


def test_analyze_text_metrics():
    """Test if metrics are calculated correctly for a standard sentence."""
    sample = "Python is a great programming language for web development."
    results = analyze_text(sample)

    assert results["word_count"] == 9
    assert results["char_count"] == 59
    assert "programming" in results["top_keywords"]


def test_reading_time_minimum():
    """Ensure very short texts return a minimum reading time of 0.01."""
    results = analyze_text("Hi")
    assert results["reading_time_minutes"] == 0.01


def test_keyword_filtering():
    """Verify that short common words are filtered out of keywords."""
    sample = "the the the code code code"
    results = analyze_text(sample)
    # 'the' is only 3 chars, so it should be filtered out based on logic
    assert "the" not in results["top_keywords"]
    assert "code" in results["top_keywords"]
