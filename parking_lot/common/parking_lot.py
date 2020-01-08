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

    def leave_car(self, slot_num: int):
        """
        Leaves the car according to the slot number
        @param slot_num: <int> slot_number to leave car
        """
        try:
            self._car_list[slot_num - 1] = None
            print('Slot number {} is free'.format(slot_num))
        except IndexError or TypeError:
            print('Please enter a valid slot number that is in this parking lot.')

    def park_car(self, registration_id: str, colour: str):
        """
        Parks car into the parking lot
        @param registration_id: <str> registration id of the car
        @param colour: <str> colour of the car
        """
        # check if the parking lot is full
        car = Car(registration_id, colour)
        if self.is_full():
            print('Sorry, parking lot is full.\n')
            return
        # get first non-None index
        first_available = [i for i in range(len(self._car_list)) if self._car_list[i] is None][0]

        self._car_list[first_available] = car

        # print out the parked place, starting from 1 to n
        print('Allocated slot number: {}'.format(first_available + 1))

    def registration_numbers_for_cars_with_colour(self, colour: str):
        """
        Gets the registration numbers for cars with input colour
        @param colour: colour to be queried
        @return <list> of registration numbers
        """
        result_list = []
        for car in self._car_list:
            if car.get_colour() == colour:
                result_list.append(car.get_plate_number())
        print(', '.join(result_list))
        return result_list

    def show_status(self):
        """
        Shows the status of our parking lot
        """
        print('Slot No. Registration No Colour\n')
        for i, car in list(enumerate(self._car_list)):
            if car is not None:
                print('{} {} {}'.format(i + 1, car.get_plate_number(), car.get_colour()))

    def slot_numbers_for_cars_with_colour(self, colour: str):
        """
        Gets slot number of cars with input colour
        @return: <list> of slot numbers
        """
        result_list = []
        for i, car in list(enumerate(self._car_list)):
            if car.get_colour() == colour:
                result_list.append(str(i + 1))
        print(', '.join(result_list))
        return result_list

    def slot_number_for_registration_number(self, registration_num: str):
        """
        Gets slot number for cars with input registration number
        @return:
        """
        result_list = []
        for i, car in list(enumerate(self._car_list)):
            if car.get_plate_number() == registration_num:
                result_list.append(str(i + 1))
        print(', '.join(result_list))
        return result_list
