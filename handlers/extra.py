from config import bot
from aiogram import types, Dispatcher, F
from aiogram.filters.command import Command

from services.extra import service_cmd_help


async def cmd_help(message: types.Message) -> None:
    await service_cmd_help(bot=bot, message=message)


def extra_register_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_help, Command('help'))
