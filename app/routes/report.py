import os
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db, UserReportDB

router = APIRouter()

# --- BULLETPROOF PATH ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

# Report Route (Loads report.html)
@router.get("/color-report/{name}", response_class=HTMLResponse)
async def get_report(request: Request, name: str, db: Session = Depends(get_db)):
    
    db_user = db.query(UserReportDB).filter(UserReportDB.name == name).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "report": db_user.report_data 
        }
    )