from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any

from aiogram.dispatcher.flags import extract_flags
from settings import ADMINS
from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


class AdminOnlyMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        flags = extract_flags(data)
        if flags.get('admin_only'):
            user_id = event.from_user.id
            username = event.from_user.username
            if int(user_id) not in ADMINS:
                logger.warning(f"User {user_id} | {username} is not admin!")
                await event.answer("You're not admin!")  # optional
                return

        return await handler(event, data)
