from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class BaseOrm(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        onupdate=datetime.now(),
    )