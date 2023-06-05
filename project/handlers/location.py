from aiogram import Router, F
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from generics.callback_factories import NearbySettingsCallbackFactory
from generics.states import OrderFood
from keyboards.reply_keyboard import ReplyKeyboardMarkup
from services.nearby import get_nearby_places
from settings import PLACE_TYPES
from utils import answer_user_location

location_router = Router()


@location_router.message(F.location, OrderFood.share_location)
async def handle_location(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    await state.set_data({'latitude': lat, 'longitude': lon})
    await message.answer('Локация сохранена', reply_markup=ReplyKeyboardMarkup.location_keyboard())
    await answer_user_location(lat, lon, message)


@location_router.message(F.text == 'Назад в меню')
async def handle_back_menu(message: Message):
    await message.answer('', reply_markup=ReplyKeyboardMarkup.location_keyboard())


@location_router.message(F.text == 'Сохраненная геолокация')
async def handle_get_location(message: Message, state: FSMContext):
    location = await state.get_data()
    if location:
        latitude = location['latitude']
        longitude = location['longitude']
        await message.answer_location(latitude=latitude, longitude=longitude)
    else:
        await message.answer('Нет информации про вашу локацию')


@location_router.callback_query(NearbySettingsCallbackFactory.filter(F.action == 'radius'))
async def callback_radius(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(OrderFood.choosing_radius)
    await callback.message.reply('Введите радиус в метрах', reply_markup=ReplyKeyboardMarkup.back_to_menu_keyboard())
    await callback.answer()


@location_router.message(F.text.func(str.isdecimal), OrderFood.choosing_radius)
async def handle_radius(message: Message, state: FSMContext):
    await state.update_data(radius=int(message.text))
    await state.set_state(OrderFood.share_location)
    await message.reply('Радиус сохранен', reply_markup=ReplyKeyboardMarkup.location_keyboard())
    state_data = await state.get_data()
    lat = state_data['latitude']
    lon = state_data['longitude']
    await answer_user_location(lat, lon, message)


@location_router.callback_query(NearbySettingsCallbackFactory.filter(F.action == 'type'))
async def callback_type(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(OrderFood.choosing_type_location)
    await callback.message.reply('Введите тип', reply_markup=ReplyKeyboardMarkup.types_choices_keyboard())
    await callback.answer()


@location_router.message(F.text.in_(PLACE_TYPES), OrderFood.choosing_type_location)
async def handle_type(message: Message, state: FSMContext):
    await state.update_data(type_location=PLACE_TYPES[message.text])
    await state.set_state(OrderFood.share_location)
    await message.answer('Тип сохраненен', reply_markup=ReplyKeyboardMarkup.location_keyboard())
    state_data = await state.get_data()
    lat = state_data['latitude']
    lon = state_data['longitude']
    await answer_user_location(lat, lon, message)


@location_router.message(OrderFood.choosing_type_location)
async def invalid_handle_type(message: Message):
    await message.answer('Не валидный тип для гугл карт')


@location_router.message(F.text, OrderFood.choosing_keyword)
async def handle_keyword(message: Message, state: FSMContext):
    await state.update_data(keyword=message.text)
    await state.set_state(OrderFood.share_location)
    await message.answer('Ключевое слово сохраненено', reply_markup=ReplyKeyboardMarkup.location_keyboard())
    state_data = await state.get_data()
    lat = state_data['latitude']
    lon = state_data['longitude']
    await answer_user_location(lat, lon, message)


@location_router.callback_query(NearbySettingsCallbackFactory.filter(F.action == 'keyword'))
async def callback_keyword(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(OrderFood.choosing_keyword)
    await callback.message.reply(
        'Введите ключевые слова для поиска',
        reply_markup=ReplyKeyboardMarkup.back_to_menu_keyboard(),
    )
    await callback.answer('Введите ключевые слова для поиска')


@location_router.message(F.text == 'Сбросить данные')
@location_router.message(Command(commands=['reset']))
async def handle_reset(
    message: Message,
    state: FSMContext,
):
    await state.set_data({})
    await state.set_state(OrderFood.share_location)
    await message.answer('Даные сброшенны')


@location_router.message(F.text == 'Получить места рядом')
async def handle_get_nearby_places(
    message: Message,
    state: FSMContext,
):
    user_data = await state.get_data()
    nearby_places = get_nearby_places(
        **user_data
    )
    if not nearby_places:
        await message.answer('Открытых заведений не найденно')
        return
    await message.answer('\n'.join((i['name'] for i in nearby_places)))
