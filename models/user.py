#!/usr/bin/python3
"""
this module is for defining class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
