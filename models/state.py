#!/usr/bin/python3
"""
defining State class the inherits from BaseModel
"""
from models.base_model import BaseModel



class State(BaseModel):
    """this class inherts from BaseModel"""
    
    self.name = name
    def __init__(self, *args, **kwargs):
        """defines a new instance from the State Class"""
        super().__init__(*args, **kwargs)
        """ensures the parent class works properly"""
