from aiogram.fsm.state import StatesGroup, State


class OrderFood(StatesGroup):
    share_location = State()
    choosing_radius = State()
    choosing_type_location = State()
    choosing_keyword = State()
