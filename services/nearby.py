from settings import GMAPS


def get_nearby_places(location, radius, type_location, key_word=None):
    response = GMAPS.places_nearby(
        location=location,
        radius=radius,
        type=type_location,
        keyword=key_word,
        language='uk',
        open_now=True,
    )
    return response['results']