from aiogram import Bot
from aiogram.types import Message

from database.crud import create_new_user
from database.db import get_session
from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


async def service_cmd_start(bot: Bot, message: Message) -> None:
    async for session in get_session():
        await create_new_user(
            session=session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.full_name,
            is_premium=message.from_user.is_premium,
        )

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"👋 Sup, {message.from_user.first_name}!"
    )
