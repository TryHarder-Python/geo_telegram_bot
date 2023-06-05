from project.settings import GMAPS


def get_nearby_places(latitude, longitude, radius=200, type_location=None, keyword=None):
    response = GMAPS.places_nearby(
        location=(latitude, longitude),
        radius=radius,
        type=type_location,
        keyword=keyword,
        language='uk',
        open_now=True,
    )
    return response['results']
