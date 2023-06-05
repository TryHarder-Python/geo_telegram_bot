from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from generics.callback_factories import NearbySettingsCallbackFactory
from settings import PLACE_TYPES


class ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder

    @classmethod
    def start_keyboard(cls):
        menu_builder = cls.keyboard_builder()
        menu_builder.button(
            text='Отдать геолокацию',
            request_location=True,
        )
        return menu_builder.as_markup(resize_keyboard=True)

    @classmethod
    def back_to_menu_keyboard(cls):
        menu_builder = cls.keyboard_builder()
        menu_builder.add(
            KeyboardButton(text='Назад в меню'),
        )
        return menu_builder.as_markup(resize_keyboard=True)

    @classmethod
    def types_choices_keyboard(cls):
        menu_builder = cls.keyboard_builder()
        buttons = [KeyboardButton(text=i) for i in PLACE_TYPES.keys()][:20]
        menu_builder.row(
            *buttons,
            width=4
        )
        menu_builder.row(KeyboardButton(text='Назад в меню'), width=1)
        return menu_builder.as_markup(resize_keyboard=True)

    @classmethod
    def location_keyboard(cls):
        menu_builder = cls.keyboard_builder()
        menu_builder.add(
            KeyboardButton(text='Обновить геолокацию', request_location=True),
            KeyboardButton(text='Сохраненная геолокация'),
            KeyboardButton(text='Получить места рядом'),
        )
        menu_builder.adjust(2)
        return menu_builder.as_markup(resize_keyboard=True)


class InlineKeyboardMarkup:
    inline_builder = InlineKeyboardBuilder

    @classmethod
    def location_keyboard(cls):
        menu_builder = cls.inline_builder()
        menu_builder.button(
            text='Радиус в метрах',
            callback_data=NearbySettingsCallbackFactory(action='radius'),
        )
        menu_builder.button(
            text='Тип места', callback_data=NearbySettingsCallbackFactory(action='type'),
        )
        menu_builder.button(
            text='Ключевое слово',
            callback_data=NearbySettingsCallbackFactory(action='keyword'),
        )
        menu_builder.adjust(2)
        return menu_builder.as_markup()
