#!/usr/bin/python3
"""User Class container"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
