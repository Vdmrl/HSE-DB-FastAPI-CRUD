from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from database.database import cursor

router = APIRouter(
    prefix="",
    tags=["CRUD"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_members(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/members", response_class=HTMLResponse)
def get_members(request: Request):
    cursor.execute("SELECT * FROM members;")
    data = cursor.fetchall()
    return templates.TemplateResponse("members_user.html", {"request": request, "data": data})


@router.get("/trainers", response_class=HTMLResponse)
def get_trainers(request: Request):
    cursor.execute(
        "SELECT trainers.id,trainers.surname,trainers.name,trainers.patronymic,trainers.birth_date,ranks.name,ranks.payment FROM trainers INNER JOIN ranks ON trainers.rank_id = ranks.id")
    data = cursor.fetchall()
    return templates.TemplateResponse("trainers_user.html", {"request": request, "data": data})


@router.get("/classes", response_class=HTMLResponse)
def get_classes(request: Request):
    cursor.execute("SELECT * FROM classes;")
    data = cursor.fetchall()
    return templates.TemplateResponse("classes_user.html", {"request": request, "data": data})


@router.get("/events", response_class=HTMLResponse)
def get_events(request: Request):
    cursor.execute("SELECT * FROM events;")
    data = cursor.fetchall()
    return templates.TemplateResponse("events_user.html", {"request": request, "data": data})


@router.get("/records", response_class=HTMLResponse)
def get_records(request: Request):
    cursor.execute("SELECT * FROM records;")
    data = cursor.fetchall()
    return templates.TemplateResponse("records_user.html", {"request": request, "data": data})
