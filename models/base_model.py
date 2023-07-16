#!/usr/bin/python3
"""This file contain BaseModel class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        __init__ metehod of the class
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ this method returns a str rep of an instance
        Returns:
        [str]: representation of a string """
        st = "[{:s}] ({:s}) {}"
        return st.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        save info to a json file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict returns the reprsentation of an instance

        Returns:
            [dict]: basemodel basic represantion dictionary
        """
        new = dict(self.__dict__)
        new["__class__"] = type(self).__name__
        new["created_at"] = new["created_at"].isoformat()
        new["updated_at"] = new["updated_at"].isoformat()

        return new
