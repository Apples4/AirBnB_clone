#!/usr/bin/python3
""" Importing depandancies """
from models.base_model import BaseModel


class User(BaseModel):
    """ inheritance class user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
