from config import bot
from aiogram import types, Dispatcher, F
from aiogram.filters.command import Command
from services.admin import service_admin_panel


async def cmd_start(message: types.Message) -> None:
    await service_admin_panel(bot=bot, message=message)


def admin_register_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start, Command("admin_panel"), flags={'admin_only': True})
