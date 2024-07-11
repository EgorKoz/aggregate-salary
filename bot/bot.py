"""Module of entry point"""
import logging
import os
from json import loads

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from bot.constant import REQUEST_PATTERN, ERROR_STRING
from utils.functions import get_aggregated_salary


dp = Dispatcher()
bot = Bot(token=os.getenv('TOKEN_BOT'))


@dp.message(Command('start'))
async def start_command_handler(message: Message) -> None:
    """Handler for command start"""
    user_mention = message.from_user.mention_html()

    await message.answer(f'Hi {user_mention}!', parse_mode='HTML')


@dp.message()
async def other_data_handler(message: Message) -> Message | None:
    """Handler for other command"""
    logging.info(f'new msq: {message.text}')
    if not REQUEST_PATTERN.search(message.text):
        return await message.answer(ERROR_STRING)

    answer = get_aggregated_salary(params=loads(message.text))

    await message.answer(answer)


async def main():
    await dp.start_polling(bot)
