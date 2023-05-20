from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply_keyboard import ReplyKeyboardMarkup

start_router = Router()


@start_router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    await message.answer(
        f"Привет, <b>{message.from_user.full_name}</b>! Я бот который помогает найти место на картке",
        reply_markup=ReplyKeyboardMarkup.start_keyboard(),
    )


@start_router.message(F.location)
async def handle_location(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    await state.set_data({'latitude': lat, 'longitude': lon})
    await message.answer('Локация сохранена', reply_markup=types.ReplyKeyboardRemove())


@start_router.message(Command(commands=["get_location"]))
async def handle_get_location(message: types.Message, state: FSMContext):
    location = await state.get_data()
    if location:
        latitude = location['latitude']
        longitude = location['longitude']
        await message.answer(f"Your saved location: Latitude: {latitude}, Longitude: {longitude}")
    else:
        await message.answer("No location found.")
