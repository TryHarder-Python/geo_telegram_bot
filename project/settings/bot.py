import os

from aiogram import Bot
from aiogram.fsm.storage.redis import RedisStorage

TOKEN = os.getenv('TOKEN')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6377')

STORAGE = RedisStorage.from_url(REDIS_URL + '/0')

BOT = Bot(TOKEN, parse_mode='HTML')
