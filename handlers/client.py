from aiogram import Dispatcher, types
from aiogram.filters.command import Command

from config import bot


# ----------------------------------- TOOLS ----------------------------------- #

async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'hello world! ;)')


def client_register_handlers(dp: Dispatcher):
    # Tools
    dp.message.register(cmd_start, Command('start'))
