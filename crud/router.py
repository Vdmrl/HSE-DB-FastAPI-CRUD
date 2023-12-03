from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from database.database import cursor

router = APIRouter(
    prefix="",
    tags=["CRUD"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/trainers", response_class=HTMLResponse)
def get_base_page(request: Request):
    cursor.execute("SELECT * FROM trainers;")
    data = cursor.fetchall()
    return templates.TemplateResponse("trainers.html", {"request": request, "data": data})
