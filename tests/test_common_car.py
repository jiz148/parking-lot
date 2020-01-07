import unittest
from unittest.mock import patch

from parking_lot.common.car import Car


class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.example_id = 'KA-01-HH-7777'
        pass

    def test___init__(self):
        """
        test parking_lot_common_car :: Car :: __init__
        """
        tests = [{
            'id': 'KA-01-HH-9999',
            'color': 'White',
            'result': ('KA-01-HH-9999', 'White'),
        }, {
            'id': 'CA-01-BB-0001',
            'color': 'Black',
            'result': ('CA-01-BB-0001', 'Black'),
        }, {
            'id': self.example_id,
            'color': 99,
            'result': (self.example_id, '99'),
        }, {
            'id': self.example_id,
            'color': 99.999,
            'result': (self.example_id, '99.999'),
        }, {
            'id': self.example_id,
            'color': bool,
            'result': (self.example_id, "<class 'bool'>"),
        }, {
            'id': self.example_id,
            'color': [],
            'result': (self.example_id, '[]'),
        }, {
            'id': self.example_id,
            'color': None,
            'result': (self.example_id, 'None'),
        }, ]
        for test in tests:
            car = Car(test.get('id'), test.get('color'))
            expected = test.get('result')
            returned = (car._plate_id, car._colour)
            self.assertEqual(expected, returned)

        # test wrong plate number, should prompt for input
        tests_wrong_plate = ['white',
                             'wrong input',
                             'some string',
                             1.5,
                             1,
                             str,
                             None]
        for test in tests:
            with patch('builtins.input', side_effect=[self.example_id]) as mock_input:
                Car(test, 'White')
            mock_input.assert_called()

    @staticmethod
    def _get_car():
        return Car()
