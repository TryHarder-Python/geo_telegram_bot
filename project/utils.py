from aiogram.types import Message

from keyboards.reply_keyboard import InlineKeyboardMarkup


async def answer_user_location(lat: float, lon: float, message: Message) -> None:
    await message.answer_location(latitude=lat, longitude=lon, reply_markup=InlineKeyboardMarkup.location_keyboard())
