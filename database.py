from sqlalchemy import Integer, String, Float, Boolean
from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class DB(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    napravlenie: Mapped[bool] = mapped_column(Boolean, nullable=False)
    tgid: Mapped[int] = mapped_column(Integer, primary_key=True)
