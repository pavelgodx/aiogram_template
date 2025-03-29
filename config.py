from settings import API_BOT_KEY
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

bot: Bot = Bot(token=API_BOT_KEY)
dp: Dispatcher = Dispatcher(storage=MemoryStorage())
