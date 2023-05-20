from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ReplyKeyboardMarkup:
    menu_builder = ReplyKeyboardBuilder()

    @classmethod
    def start_keyboard(cls):

        cls.menu_builder.button(
            text='Отдать геолокацию',
            request_location=True,
        )
        return cls.menu_builder.as_markup()
