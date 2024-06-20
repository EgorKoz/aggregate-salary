"""Module of entry point"""
from json import loads
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from bot.constant import *
from utils.functions import get_aggregate_salary


dp = Dispatcher()
bot = Bot(token=getenv('BOT_TOKEN'))


@dp.message(Command('start'))
async def welcome(message: Message) -> None:
    """Handler for command start"""
    user_mention = message.from_user.mention_html()

    await message.answer(f'Hi {user_mention}!', parse_mode='HTML')


@dp.message()
async def print_response_from_db(message: Message) -> Message | None:
    if not REQUEST_PATTERN.search(message.text):
        return await message.answer(ERROR_STRING)

    answer = get_aggregate_salary(params=loads(message.text))

    await message.answer(answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
