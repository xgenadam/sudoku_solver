from only_choice import only_choice
from utils import eliminate, display
from reduce_ideal import reduce_puzzle as ideal_reduce

test_values = {
    'I5': '1',
    'C7': '4',
    'A3': '3',
    'H7': '123456789',
    'E2': '123456789',
    'E3': '123456789',
    'F5': '123456789',
    'D1': '123456789',
    'I3': '5',
    'I2': '123456789',
    'F3': '6',
    'E1': '7',
    'B2': '123456789',
    'H5': '123456789',
    'B3': '123456789',
    'E8': '123456789',
    'C4': '8',
    'A2': '123456789',
    'G3': '2',
    'E9': '8',
    'D3': '8',
    'C2': '123456789',
    'C8': '123456789',
    'I6': '123456789',
    'A1': '123456789',
    'C3': '1',
    'E6': '123456789',
    'E7': '123456789',
    'I7': '3',
    'D6': '2',
    'H3': '123456789',
    'G9': '123456789',
    'G7': '5',
    'H2': '123456789',
    'I4': '123456789',
    'B5': '123456789',
    'C1': '123456789',
    'A7': '6',
    'D4': '1',
    'H1': '8',
    'F9': '123456789',
    'C9': '123456789',
    'D2': '123456789',
    'D7': '9',
    'G2': '123456789',
    'F2': '123456789',
    'H4': '2',
    'I9': '123456789',
    'F7': '2',
    'H9': '9',
    'F8': '123456789',
    'I1': '123456789',
    'A4': '123456789',
    'G1': '123456789',
    'G5': '123456789',
    'G4': '6',
    'G6': '9',
    'E5': '123456789',
    'F4': '7',
    'B1': '9',
    'B4': '3',
    'A9': '123456789',
    'B7': '123456789',
    'F1': '123456789',
    'D5': '123456789',
    'F6': '8',
    'B6': '5',
    'D9': '123456789',
    'H6': '3',
    'C6': '6',
    'A6': '123456789',
    'C5': '123456789',
    'G8': '123456789',
    'B9': '1',
    'A8': '123456789',
    'B8': '123456789',
    'I8': '123456789',
    'E4': '123456789',
    'A5': '2',
    'D8': '123456789',
    'H8': '123456789'
}

class BrokenSudokuException(Exception):
    pass


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = (solved_values_before == solved_values_after)
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


if __name__ == '__main__':
    display(test_values)
    print('personal reduce')
    personal_reduce = reduce_puzzle(test_values)
    display(personal_reduce)
    print('\n')
    print('ideal_reduce')
    ideal = ideal_reduce(test_values)
    display(ideal)

    print(personal_reduce == ideal)
    assert personal_reduce == ideal