from fastapi import FastAPI
from app.routes import analyze, report

app = FastAPI(title="ChromaID API")

# Include routes
app.include_router(analyze.router)
app.include_router(report.router)