# utils.py
from enum import Enum
import re
import os

def get_absolute_path(filepath: str) -> str:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = ROOT_DIR.replace('utilities', filepath)
    return ROOT_DIR

PLANET_IMAGE = '/data/images/planets/earth.jpg'

# Colours
ORANGE = 0x006A86E4
GREEN = 0x00ABCC7D
GREY = 0x00EDE8EA
BLACK = 0x00271D18
BLUE = 0x00EBC299
    

class Action(Enum):
    """An Enum for the Response Actions."""
    DISPLAY = 0
    COMPARE = 1
    RESPOND = 2

class Detail(Enum):
    """An Enum for the Response Details."""
    ALL = 0
    FACT = 1

class Fact(Enum):
    """An Enum for the Response Facts."""
    ALL = 0
    MASS = 1
    DISTANCE = 2
    SATELLITES = 3
    MOONS = 4
    RADIUS = 5

class Planet(Enum):
    """An Enum for the Response Planets."""
    ALL = 0
    MERCURY = 1
    VENUS = 2
    EARTH = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8

def sanitize_query(query: str) -> list[str]:
    """Raw user input is removed of special characters and split into atomic parts.
    
    :param str query: A raw user query received from the console.
    
    :return: The sanitised list of user input words.
    :rtype: list[str]
    
    .. impl::
        :id: UTL_SANITIZE_QUERY
        :implements: REQ001
        :tests: TTS001
    """
    split_message: list[str] = list(re.split(r'\s+|[?.,\';:-]\s*', query.lower()))
    for item in split_message:
        item = item.strip()