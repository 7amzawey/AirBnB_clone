#!/usr/bin/python3
"""Base Model that Defines all common attributes/methods for other classes."""


from datetime import datetime
import uuid


class BaseModel():
    """Base Model for all other attributes and methods."""

    def __init__(self):
        """Initialize the attributes of the base model."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print class_name, id, self.__dict__."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary representation of an object."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
