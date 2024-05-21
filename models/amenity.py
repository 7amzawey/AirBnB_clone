#!/usr/bin/python3
"""defines an Amenity class the inherits from BaseModel"""
from models.base_model import BaseModel



class Amenity(BaseModel):
    """defines a new class Amenity that inherits from BaseModel"""
    name = ""
    def __init__(self, *args, **kwargs):
        """creates a new instance from the Amenity class"""
        super().__init__(*args, **kwargs)
