#!/usr/bin/python3
"""defines a place class the inherits from BaseModel"""
from models.base_model import BaseModel



class Place(BaseModel):
    """defines a new class Amenity that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """creates a new instance from the Amenity class"""
        super().__init__(*args, **kwargs)
