# FastAI CRUD with raw SQL

This repostiroty creates simple crud using [FastAPI framework](https://fastapi.tiangolo.com/),
data validated with [pydantic](https://github.com/pydantic/pydantic)
cookies JWT token authentication with [FastAPI-users](https://github.com/fastapi-users/fastapi-users),
PostgreSQL databsase connection using raw [psycopg](https://github.com/psycopg/psycopg) and [SQLalchemy](https://github.com/sqlalchemy/sqlalchemy) with [Alembic](https://github.com/sqlalchemy/alembic) 
frontend with html, css, [tailwindcss](https://github.com/tailwindlabs/tailwindcss) and [jinja 2 templates](https://github.com/pallets/jinja/)

![Screenshot of crud](readme_crud.png)

![Screenshot of registration](readme_registration.png)

## Opening the project

1. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it.

2. Install requirements:

    ```shell
    python3 -m pip install --user -r requirements-dev.txt
    ```

3. Run server using uvicorn:

   ```shell
    uvicorn main:app --reload 
    ```
