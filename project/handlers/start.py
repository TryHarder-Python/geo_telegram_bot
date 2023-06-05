from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from generics.states import OrderFood
from keyboards.reply_keyboard import ReplyKeyboardMarkup

start_router = Router()


@start_router.message(Command(commands=['start']))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receive messages with `/start` command
    """

    await message.answer(
        f'Привет, <b>{message.from_user.full_name}</b>! Я бот который помогает найти место на картке',
        reply_markup=ReplyKeyboardMarkup.start_keyboard(),
    )
    await state.set_state(OrderFood.share_location)
