from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.models.schemas import AnalyzeResponse
from app.services.color_service import analyze_user, generate_report, user_store

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    name: str = Form(...),
    photo: UploadFile = File(...)
):
    # Basic validation
    if not photo.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    season_type = analyze_user(name)

    # Generate full report
    report = generate_report(season_type)

    # Store result
    user_store[name] = report

    return AnalyzeResponse(
        name=name,
        season_type=season_type
    )