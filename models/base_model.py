#!/usr/bin/python3
"""BaseModel class"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Representing basemodel"""

    def __init__(self):
        """Initializing an attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[" + str(__name__) + "] " + "(" + str(self.id) + ")"
                + str(self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        ndict = self.__dict__.copy()
        ndict["__class__"] = self.__class__.__name__
        ndict["created_at"] = self.created_at.isoformat("T")
        ndict["updated_at"] = self.updated_at.isoformat("T")
        return ndict
