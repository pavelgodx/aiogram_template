import time
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any

from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


class RateLimitMiddleware(BaseMiddleware):
    def __init__(self, default_delay: float = 2.0):
        self.default_delay = default_delay
        self.last_called: Dict[int, float] = {}

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        flags = data.get("handler").flags if "handler" in data else {}
        delay = flags.get("throttle", self.default_delay)

        user_id = event.from_user.id
        now = time.monotonic()

        last_time = self.last_called.get(user_id, 0)
        if now - last_time < delay:
            logger.info(f"Rate limit: user {user_id} too fast (limit = {delay}s)")
            await event.answer(
                f"⏳ Please, wait {round(delay - (now - last_time), 1)} seconds to use further a bot.")  # optional
            return

        self.last_called[user_id] = now
        return await handler(event, data)
