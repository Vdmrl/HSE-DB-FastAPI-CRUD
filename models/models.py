from sqlalchemy import Boolean, Column, Integer, String, MetaData, Table

metadata = MetaData()
user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, index=True, nullable=False),
    Column("email", String(length=320), unique=True, index=True, nullable=False),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)