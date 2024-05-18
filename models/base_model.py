#!/usr/bin/python3
import uuid
import datetime
from models import storage
"""
This Module is for Defining a class BaseModel which defines all the other
common attributes for other classes.
"""


class BaseModel:
    """this class defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """you will use *args, **kwargs arguments for
        the constructor of a BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'updated_at' or key == 'created_at':
                        value = datetime.datetime.strptime(
                                value,
                                "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """this should print [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """updates the public instance attribute withe the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionarey containing all keys/values of __dict__ of the
        instance"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
