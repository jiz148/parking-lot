"""
parking_lot.py
Main interface of project: parking lot
"""
import os
import sys

from common.parking_lot import ParkingLot

FILE_INPUT = sys.argv[1] if len(sys.argv) > 1 else None


class Main:

    def __init__(self):
        self.parking_lot = None
        pass

    def _command_to_call_function(self, command: str):
        """
        Parses a string to perform
        @param: command to be parsed
        """
        try:
            word_list = command.strip().split()
            func_str = word_list.pop(0)
            if func_str == 'create_parking_lot':
                self.parking_lot = ParkingLot(int(word_list[0]))
                return
            param_str = '", "'.join(word_list)
            if not param_str:
                command_str = 'self.parking_lot.' + func_str + '(' + param_str + ')'
            else:
                command_str = 'self.parking_lot.' + func_str + '("' + param_str + '")'
            print(command_str)
            eval(command_str)
        except Exception:
            print('Invalid Input')
        pass


def run_without_interaction():
    print('passed here')
    print('Please start to enter commands\n'
          'create_parking_lot <number of slots> first to create a parking lot\n'
          'q to quit...\n')
    main = Main()
    q = False
    while not q:
        command = input()
        if command != 'q':
            main._command_to_call_function(command)
        else:
            q = True
    print('Exited.')


def run_with_interaction():
    main = Main()
    file_path = os.path.dirname(os.path.realpath(__file__))
    repo_path = os.path.dirname(file_path) # hard coded here, assuming file is in root
    txt_path = os.path.join(repo_path, FILE_INPUT)
    with open(txt_path) as file:
        line = file.readline()
        while line:
            main._command_to_call_function(line)
            line = file.readline()


if __name__ == "__main__":
    if not FILE_INPUT:
        run_without_interaction()
    else:
        run_with_interaction()
