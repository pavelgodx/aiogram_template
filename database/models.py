import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base  # ✅ Новый импорт

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String)
    full_name = Column(String)
    is_premium = Column(Boolean)
    registered_at = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.UTC))
