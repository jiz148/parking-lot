import unittest

from parking_lot.common.car import Car
from parking_lot.common.parking_lot import ParkingLot


class TestParkingLot(unittest.TestCase):

    def setUp(self) -> None:
        self.example_size = 10
        self.example_car_id = 'KA-01-HH-7777'
        self.example_car_colour = 'White'
        self.example_car = Car(self.example_car_id, self.example_car_colour)
        self.example_different_car = Car(self.example_car_id, 'Black')

    def test_is_full(self):
        """
        test parking_lot.common.parking_lot :: ParkingLot :: is_full
        """
        tests = [{
            'element': self.example_car,
            'returned': True,
        }, {
            'element': 'car',
            'returned': True,
        }, {
            'element': 1,
            'returned': True,
        }, {
            'element': int,
            'returned': True,
        }, {
            'element': None,
            'returned': False,
        }]
        for test in tests:
            parking_lot = self._create_parking_lot()
            parking_lot._car_list = [test.get('element')] * self.example_size
            expected = test.get('returned')
            returned = parking_lot.is_full()
            self.assertEqual(expected, returned)

    def test_park_car(self):
        """
        test parking_lot.common.parking_lot :: ParkingLot :: park_car
        """
        tests = [{
            'car_list': self._create_car_list([0, 1, 2]),
            'spot': 0,
        }, {
            'car_list': self._create_car_list([4, 6, 7]),
            'spot': 4,
        }, {
            'car_list': self._create_car_list([7]),
            'spot': 7,
        }, {
            'car_list': self._create_car_list([1, 2, 3, 4, 5, 6, 7]),
            'spot': 1,
        }, {
            'car_list': [self.example_car, self.example_car],
            'spot': None,
        }]
        for test in tests:
            parking_lot = self._create_parking_lot()
            parking_lot._car_list = test.get('car_list')
            parking_lot.park_car(self.example_different_car)
            spot = test.get('spot')
            if spot is not None:
                self.assertEqual(self.example_different_car.get_colour(), parking_lot._car_list[spot].get_colour())
            else:
                for item in parking_lot._car_list:
                    self.assertEqual(self.example_car.get_colour(), item.get_colour())

    def _create_parking_lot(self):
        return ParkingLot(self.example_size)

    def _create_car_list(self, empty_spot_list: list):
        """
        Creates car list with list of spots being None
        while other spots are example cars
        @param empty_spot_list: <list[int]> list of spots where it is None
        @return: <list>car list
        """
        car_list = [self.example_car] * self.example_size
        for index in empty_spot_list:
            car_list[index] = None
        return car_list
