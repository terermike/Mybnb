#!/usr/bin/python3
"""This script is the base model"""

import os, json

class FileStorage:
    """Manages serialization and desirialization of instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8" ) as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        '''Reloads the stored objects'''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            FileStorage.__objects = obj_dict
    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.bas_model import BaseModel
        classes = {
        "BaseModel" : Basemodel}
        return classes
        
