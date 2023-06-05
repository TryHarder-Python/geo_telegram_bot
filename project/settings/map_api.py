import os

import googlemaps

GOOGLE_MAP_API_KEY = os.getenv('GOOGLE_MAP_API_KEY')

GMAPS = googlemaps.Client(key=GOOGLE_MAP_API_KEY)
PLACE_TYPES = {
    'Ресторани': 'restaurant',
    'Кафе': 'cafe',
    'Бари': 'bar',
    'Нічні клуби': 'night_club',
    'Кінотеатри': 'movie_theater',
    'Музеї': 'museum',
    'Торгові центри': 'shopping_mall',
    'Парки розваг': 'amusement_park',
    'Банкомати': 'atm',
    'Аптеки': 'drugstore',
    'Зоомагазини': 'pet_store',
    'Парки': 'park',
    'Аеропорти': 'airport',
    'Автостанції': 'bus_station',
    'Залізничні вокзали': 'train_station',
    'Метро': 'subway_station',
    'Таксі': 'taxi_stand',
    'Парковки': 'parking',
    'Готелі': 'lodging',
    'Школи': 'school',
    'Університети': 'university',
    'Бібліотеки': 'library',
    'Лікарні': 'hospital',
    'Поліція': 'police',
    'Пошта': 'post_office',
    'Газові заправки': 'gas_station',
    'Автомийки': 'car_wash',
    'Автосалони': 'car_dealer',
    'Автосервіси': 'car_repair',
    'Автостоянки': 'parking',
    'Автобусні зупинки': 'bus_station',
    'Автозаправки': 'gas_station',
}
