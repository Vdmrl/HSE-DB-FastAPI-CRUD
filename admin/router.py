from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from starlette.responses import HTMLResponse

from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

from database.database import cursor, connection

from admin.scemas import Member

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

templates = Jinja2Templates(directory="templates")


@router.get("", response_class=HTMLResponse)
def get_base_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/registration", response_class=HTMLResponse)
def get_base_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.get("/members", response_class=HTMLResponse)
def get_members(request: Request, user: User = Depends(current_user)):
    cursor.execute("SELECT * FROM members;")
    data = cursor.fetchall()
    return templates.TemplateResponse("members_admin.html", {"request": request, "data": data, "user": user})

@router.post("/members")
def get_members(member: Member, user: User = Depends(current_user)):
    cursor.execute(f"INSERT INTO members VALUES (DEFAULT, '{member.surname}', '{member.name}', '{member.patronymic}', '{member.birth_date}')")
    connection.commit()
    return member


@router.get("/trainers", response_class=HTMLResponse)
def get_trainers(request: Request, user: User = Depends(current_user)):
    cursor.execute(
        "SELECT * FROM trainers")
    data = cursor.fetchall()
    return templates.TemplateResponse("trainers_admin.html", {"request": request, "data": data, "user": user})

@router.get("/ranks", response_class=HTMLResponse)
def get_trainers(request: Request, user: User = Depends(current_user)):
    cursor.execute(
        "SELECT * FROM ranks")
    data = cursor.fetchall()
    return templates.TemplateResponse("ranks_admin.html", {"request": request, "data": data, "user": user})


@router.get("/classes", response_class=HTMLResponse)
def get_classes(request: Request, user: User = Depends(current_user)):
    cursor.execute("SELECT * FROM classes;")
    data = cursor.fetchall()
    return templates.TemplateResponse("classes_admin.html", {"request": request, "data": data, "user": user})


@router.get("/events", response_class=HTMLResponse)
def get_events(request: Request, user: User = Depends(current_user)):
    cursor.execute("SELECT * FROM events;")
    data = cursor.fetchall()
    return templates.TemplateResponse("events_admin.html", {"request": request, "data": data, "user": user})

@router.get("/participation", response_class=HTMLResponse)
def get_events(request: Request, user: User = Depends(current_user)):
    cursor.execute("SELECT * FROM participations;")
    data = cursor.fetchall()
    return templates.TemplateResponse("participation_admin.html", {"request": request, "data": data, "user": user})


@router.get("/records", response_class=HTMLResponse)
def get_records(request: Request, user: User = Depends(current_user)):
    cursor.execute("SELECT * FROM records;")
    data = cursor.fetchall()
    return templates.TemplateResponse("records_admin.html", {"request": request, "data": data, "user": user})
