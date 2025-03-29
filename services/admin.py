from aiogram import Bot
from aiogram.types import Message

from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


async def service_admin_panel(bot: Bot, message: Message) -> None:
    await bot.send_message(message.from_user.id, 'Hello, admin! ;)')
