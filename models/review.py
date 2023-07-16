#!/usr/bin/python3
"""The file contain the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review the class that succeeds BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
