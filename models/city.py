#!/user/bin/python3
"""
defines city class that inherits from BaseModel class
"""
from models.base_model import BaseModel



class City(BaseMode):
    """this class inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """this class is an instance of the City class"""
        super().__init__(*args, **kwargs)
        """makes sure the parent direcotry works properly"""
