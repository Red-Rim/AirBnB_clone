#!/usr/bin/python3
"""Defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that inherit from BaseModel"""

    state_id = ""
    name = ""
