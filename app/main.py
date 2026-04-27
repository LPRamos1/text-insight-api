from fastapi import FastAPI
from app.api.routes import analysis
from app.db.session import engine
from app.db.base import Base
from app.models.analysis import Analysis
import logging

app = FastAPI()

# Configure basic logging for the application
logging.basicConfig(level=logging.INFO)

# Register API routes
app.include_router(analysis.router, prefix="/analysis")

# Create database tables on startup (dev only)
Base.metadata.create_all(bind=engine)
