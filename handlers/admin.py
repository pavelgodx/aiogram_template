from config import bot
from aiogram import types, Dispatcher, F
from aiogram.filters.command import Command
from services.admin import service_admin_panel, service_admin_file


async def cmd_start(message: types.Message) -> None:
    await service_admin_panel(bot=bot, message=message)


async def cmd_media(message: types.Message) -> None:
    await service_admin_file(bot=bot, message=message)


def admin_register_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start, Command("admin_panel"), flags={'admin_only': True})
    dp.message.register(cmd_media, F.photo | F.video | F.animation, flags={'admin_only': True})
