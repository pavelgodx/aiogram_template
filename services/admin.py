from aiogram import Bot
from aiogram.types import Message

from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


async def service_admin_panel(bot: Bot, message: Message) -> None:
    await bot.send_message(message.from_user.id, 'Hello, admin! ;)')


async def service_admin_file(bot: Bot, message: Message) -> None:
    file_id = None

    if message.photo:
        file_id = message.photo[-1].file_id
    elif message.animation:
        file_id = message.animation.file_id
    elif message.video:
        file_id = message.video.file_id

    await message.answer(text=file_id)
