#!/usr/bin/python3
import json
"""This module is for defining a class FileStorgae that serializes instances
to a json file and deserializes json file to instances"""


class FileStorage:
    """serilizes instances to a json file and deserilaizeds json file
    to instances"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes the __objects to json file(path:__file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dict_objs = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_objs, f)

    def reload(self):
        """desearializes the json file to __objects(only if the json file
        exists in the __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                objs = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                class_map = {
                        "BaseModel": BaseModel,
                        "User": User
                        }

                for k, v in objs.items():
                    cls_name = v["__class__"]
                    if cls_name in class_map:
                        self.__objects[k] = class_map[cls_name](**v)

        except FileNotFoundError:
            pass
