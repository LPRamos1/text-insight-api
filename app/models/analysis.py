from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Analysis(Base):
    """Database model representing a text analysis."""

    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    word_count: Mapped[int] = mapped_column(Integer)
    char_count: Mapped[int] = mapped_column(Integer)
    reading_time_minutes: Mapped[float] = mapped_column(Float)
