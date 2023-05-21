import os

from aiogram import Bot
from aiogram.fsm.storage.redis import RedisStorage

TOKEN = os.getenv('TOKEN')

STORAGE = RedisStorage.from_url('redis://localhost:6379')

BOT = Bot(TOKEN, parse_mode='HTML')
