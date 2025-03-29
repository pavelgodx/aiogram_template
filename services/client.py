from aiogram import Bot
from aiogram.types import Message

# from api.openai_api import ask_chatgpt
from database.crud import create_new_user
from database.db import get_session
from keyboards.client_inline import inline_menu_example
from logging_config import LoggerFactory

logger = LoggerFactory().get_logger(__name__)


async def service_cmd_start(bot: Bot, message: Message) -> None:
    async for session in get_session():
        await create_new_user(
            session=session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.full_name,
            is_premium=message.from_user.is_premium,
        )

    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"👋 Sup, {message.from_user.first_name}!",
        reply_markup=inline_menu_example()
    )


async def service_handle_text(bot: Bot, message: Message) -> None:
    await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    # answer = ask_chatgpt(prompt=message.text)
    # if not answer:
    #     return
    # await message.answer(text=answer)
    await message.answer(text='Idk, what are u saying?🤯')
