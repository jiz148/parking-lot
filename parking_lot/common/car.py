"""
car.py
This script includes car class
"""
import re

DEFAULT_ID = 'DEFAULT_ID'
DEFAULT_COLOUR = 'DEFAULT_COLOUR'


class Car:

    def __init__(self, plate_id: str = DEFAULT_ID, colour: str = DEFAULT_COLOUR):
        """
        @param plate_id: <str> plate number of the car
        @param colour: <str> colour of the car
        """
        self._plate_id = None
        self._set_plate_num(str(plate_id))
        self._colour = str(colour)

    def get_plate_number(self):
        return self._plate_id

    def get_colour(self):
        return self._colour

    def _set_plate_num(self, plate_id: str):
        """
        Sets the plate number of the car, will validate the input string.
        if validate, set the plate id, otherwise. ask for another validate plate
        @param plate_id: <string> plate id of the car
        """
        check = re.match('([A-Z|a-z]{2}-\d{2}-[A-Z|a-z]{2}-\d{1,4})?([A-Z|a-z]{3}-\d{1,4})?', plate_id.strip())
        if check.group():
            self._plate_id = plate_id
            return
        else:
            new_plate_id = input('Please enter a valid vehicle registration number:\n')
            self._set_plate_num(str(new_plate_id))
