"""
parking_lot.py
Main interface of project: parking lot
"""


def run():
    print('Please start to enter commands, q to quit...')
    q = False
    while not q:
        command = input()
        if command != 'q':
            _command_to_call_function(command)
        else:
            q = True
    print('Exited.')


def _command_to_call_function(command: str):
    """
    Parses a string to perform
    @param: command to be parsed
    """
    try:
        word_list = command.strip().split()
        func_str = word_list.pop(0)
        param_str = ', '.join(word_list)
        command_str = func_str + '(' + param_str + ')'
        eval(command_str)
    except Exception:
        print('Invalid Input')
    pass


if __name__ == "__main__":
    run()
