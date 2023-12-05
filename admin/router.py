from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

templates = Jinja2Templates(directory="templates")


@router.get("", response_class=HTMLResponse)
def get_base_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/registration", response_class=HTMLResponse)
def get_base_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})
