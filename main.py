# python -m uvicorn main:app --reload
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.manager import get_user_manager
from crud.router import router as router_CRUD
from admin.router import router as router_admin
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.schemas import UserCreate, UserRead

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title="running club")
app.include_router(router_CRUD)
app.include_router(router_admin)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"