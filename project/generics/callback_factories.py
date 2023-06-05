from aiogram.filters.callback_data import CallbackData


class NearbySettingsCallbackFactory(CallbackData, prefix='fabnearby'):
    action: str
