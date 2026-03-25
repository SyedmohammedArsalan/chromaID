from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.schemas import AnalyzeResponse
from app.services.color_service import generate_report
from app.services.ml_service import determine_season
from app.database import get_db, UserReportDB

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    name: str = Form(...),
    photo: UploadFile = File(...),
    db: Session = Depends(get_db) # 1. Inject the database session
):
    if not photo.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Run ML and Generate Report
    image_bytes = await photo.read()
    season_type = determine_season(image_bytes)
    report = generate_report(season_type)

    # 2. Convert the Pydantic report model to a dictionary for the database
    # Note: If you get an error here, change .model_dump() to .dict()
    report_dict = report.model_dump() 

    # 3. Check if user exists, update them if they do, create new if they don't
    db_user = db.query(UserReportDB).filter(UserReportDB.name == name).first()
    
    if db_user:
        db_user.season_type = season_type
        db_user.report_data = report_dict
    else:
        new_report = UserReportDB(
            name=name,
            season_type=season_type,
            report_data=report_dict
        )
        db.add(new_report)
    
    # 4. Save changes to the database
    db.commit()

    return AnalyzeResponse(name=name, season_type=season_type)