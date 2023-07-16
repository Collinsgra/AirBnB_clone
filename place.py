#!/usr/bin/python3
"""The file contain the class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class succeeds BaseModel class
    """
    city_id = ""
    user_id = ""
    name = ""
    character = ""
    rooms_number = 0
    bathrooms_number = 0
    muximum_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

