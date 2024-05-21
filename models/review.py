#!/usr/bin/python3
"""this class is a son of the BaseModel class"""
from models.base_model import BaseModel



class Review(BaseModel):
    """defines Review that inherits from the BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """defines an instance of the BaseModel class"""

        super().__init__(*args, **kwargs)
