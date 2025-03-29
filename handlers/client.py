from aiogram import types, Dispatcher, F
from aiogram.filters.command import Command
from config import bot
from services.client import service_cmd_start


async def cmd_start(message: types.Message) -> None:
    await service_cmd_start(bot=bot, message=message)


def client_register_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start, Command('start'))
