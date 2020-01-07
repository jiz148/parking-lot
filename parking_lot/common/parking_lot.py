"""
parking_lot.py
This script includes ParkingLot class
"""
from .car import Car


class ParkingLot:

    def __init__(self, slot_amount: int):
        """
        @param slot_amount: number of slots in the parking lot
        """
        self._slot_amount = slot_amount
        self._car_list = [None] * self._slot_amount
        print('Created a parking lot with {} slots'.format(self._slot_amount))

    def is_full(self):
        """
        Checks if the parking lot is full
        @return: <bool> whether the parking lot is full
        """
        return len([i for i, val in enumerate(self._car_list) if val is not None]) == len(self._car_list)

    def park_car(self, car: Car):
        """
        Parks car into the parking lot
        @param car: <Car> Car to park in
        """
        # check if the parking lot is full
        if self.is_full():
            print('The parking lot is full.\n')
            return
        # get first non-None index
        first_available = [i for i in range(len(self._car_list)) if self._car_list[i] is None][0]

        self._car_list[first_available] = car

    def show_status(self):
        """
        Shows the status of our parking lot
        """
        print('hello world')
