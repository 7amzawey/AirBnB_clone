#!/usr/bin/python3
"""
this module is for defining class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """initilize an instance of the user classs"""
        super.__init__(*args, **kwargs)
