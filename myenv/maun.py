import logging
import sys
import asyncio
from os import getenv
from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.filters import CommandStart
from aiogram.types import ContentType

TOKEN = getenv("7803681612:AAFIIKuoh4rB47KJz38bxG38L6XoRy39XxU")

bot = Bot(token="7803681612:AAFIIKuoh4rB47KJz38bxG38L6XoRy39XxU")
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer("Привет! Это стартовая команда.")

@router.message(F.content_type == ContentType.PHOTO)
async def cmd(message: types.Message):
    await message.answer('Cool photo')


dp.include_router(router)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))


dp.include_router(router)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(dp.start_polling(bot))
