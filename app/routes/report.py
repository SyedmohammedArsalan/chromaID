from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.color_service import user_store

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/color-report/{name}", response_class=HTMLResponse)
async def get_report(request: Request, name: str):
    report = user_store.get(name)

    if not report:
        raise HTTPException(status_code=404, detail="User not found")

    # --- UPDATED SECTION BELOW ---
    return templates.TemplateResponse(
        request=request,          # 1. Explicitly pass the request
        name="report.html",       # 2. Explicitly name the template
        context={                 # 3. Pass your data in the context dictionary
            "report": report
        }
    )