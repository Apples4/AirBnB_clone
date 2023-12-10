#!/usr/bin/python3
""" Importing depandancies """
from models.base_model import BaseModel


class City(BaseModel):
    """Class for the city"""
    state_id = ""
    name = ""
