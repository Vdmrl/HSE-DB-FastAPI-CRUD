from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from starlette.responses import HTMLResponse

from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

from database.database import cursor, connection

from admin.scemas import Member_to_insert, Member_to_delete, Member_to_update

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


@router.post("/members/insert")
def get_members(member: Member_to_insert, user: User = Depends(current_user)):
    # XD
    if member.surname and member.name and member.patronymic and len(member.birth_date) == 10 and member.birth_date[
        4] == '-' and member.birth_date[4] == '-' and member.birth_date[7] == '-' and (
            1 <= int(member.birth_date[8:]) <= 31) and (1 <= int(member.birth_date[5:7]) <= 12) and (
            1900 <= int(member.birth_date[0:4]) <= 2023):
        insert_query = """
            INSERT INTO members (id, surname, name, patronymic, birth_date) 
            VALUES (DEFAULT, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_query,
            (member.surname, member.name, member.patronymic, member.birth_date)
        )

        connection.commit()
    else:
        return HTTPException(status_code=400, detail="Wrong database injection")
    return member


@router.post("/members/delete")
def get_members(member: Member_to_delete, user: User = Depends(current_user)):
    cursor.execute(f"DELETE FROM members WHERE id = {member.id}")
    connection.commit()
    return member


@router.post("/members/update")
def get_members(member: Member_to_update, user: User = Depends(current_user)):
    # XD
    if (member and member.birth_date):
        member.birth_date = member.birth_date.strip()
    cursor.execute("SELECT id FROM members")
    if int(member.id) in map(lambda x: x[0],
                             cursor.fetchall()) and member.surname and member.name and member.patronymic and len(
        member.birth_date) == 10 and member.birth_date[4] == '-' and member.birth_date[4] == '-' and \
            member.birth_date[7] == '-' and (1 <= int(member.birth_date[8:]) <= 31) and (
            1 <= int(member.birth_date[5:7]) <= 12) and (1900 <= int(member.birth_date[0:4]) <= 2023):
        print('ssfsdf')

        update_query = """
            UPDATE members 
            SET surname = %s, name = %s, patronymic = %s, birth_date = %s 
            WHERE id = %s
        """

        cursor.execute(
            update_query,
            (member.surname, member.name, member.patronymic, member.birth_date, member.id)
        )

        connection.commit()
    else:
        connection.rollback()
        return HTTPException(status_code=400, detail="Wrong database injection")
    return member
