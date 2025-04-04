import asyncio

from database.db import engine
from database.models import Base
from handlers.client import client_register_handlers
from handlers.admin import admin_register_handlers
from config import dp, bot
from aiogram.methods import DeleteWebhook

from handlers.extra import extra_register_handlers
from middlewares.admin_check import AdminOnlyMiddleware
from middlewares.rate_limit import RateLimitMiddleware


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_all() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def main() -> None:
    await drop_all()  # temporary
    await init_db()
    print(f'[{bot.id} | {await bot.get_my_name()}] is online!✅')
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    dp.message.middleware(AdminOnlyMiddleware())
    dp.message.middleware(RateLimitMiddleware(default_delay=1.5))

    admin_register_handlers(dp)
    client_register_handlers(dp)
    extra_register_handlers(dp)
    asyncio.run(main())
