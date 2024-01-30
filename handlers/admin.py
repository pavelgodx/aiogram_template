from config import bot
from aiogram import types, Dispatcher, F
from aiogram.filters.command import Command
from settings import ADMINS


async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'hello world')


def admin_register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command('admin_panel'))
