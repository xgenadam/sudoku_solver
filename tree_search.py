from ideal_tree_search import search as ideal_search
from reduce import reduce_puzzle
from utils import contains_clashes, display, serialize_grid, sudoku_solved

test_values = {
    'D4': '123456789',
    'F4': '123456789',
    'E1': '123456789',
    'A9': '5',
    'E8': '123456789',
    'G8': '7',
    'H5': '123456789',
    'B2': '3',
    'D3': '123456789',
    'B6': '123456789',
    'B5': '123456789',
    'A8': '123456789',
    'B9': '123456789',
    'D2': '2',
    'I1': '1',
    'F7': '123456789',
    'H1': '5',
    'I3': '4',
    'H4': '2',
    'A1': '4',
    'C7': '123456789',
    'F5': '1',
    'C6': '123456789',
    'B4': '123456789',
    'A3': '123456789',
    'B8': '123456789',
    'G9': '123456789',
    'I6': '123456789',
    'G7': '123456789',
    'B7': '123456789',
    'A4': '123456789',
    'A2': '123456789',
    'H2': '123456789',
    'A6': '123456789',
    'H8': '123456789',
    'F8': '123456789',
    'E7': '4',
    'A5': '123456789',
    'D8': '6',
    'F9': '123456789',
    'I9': '123456789',
    'G3': '123456789',
    'E6': '123456789',
    'I8': '123456789',
    'D1': '123456789',
    'I7': '123456789',
    'E5': '8',
    'I2': '123456789',
    'F3': '123456789',
    'G2': '123456789',
    'I4': '123456789',
    'C5': '123456789',
    'D7': '123456789',
    'C1': '123456789',
    'G1': '123456789',
    'D5': '123456789',
    'F6': '123456789',
    'G5': '123456789',
    'I5': '123456789',
    'G6': '3',
    'D9': '123456789',
    'F1': '123456789',
    'E2': '123456789',
    'A7': '8',
    'D6': '123456789',
    'C3': '123456789',
    'E3': '123456789',
    'H3': '123456789',
    'E9': '123456789',
    'H7': '123456789',
    'F2': '123456789',
    'C4': '7',
    'C2': '123456789',
    'G4': '6',
    'C8': '123456789',
    'C9': '123456789',
    'B1': '123456789',
    'H9': '123456789',
    'H6': '123456789',
    'B3': '123456789',
    'E4': '123456789'}


def location_values_filter(location, vals):
    if len(vals) > 1:
        return True

    return False


def get_location_with_least_values(values):
    sorted_values = sorted(values.items(), key=lambda x: len(x[1]))
    ordered_values = filter(lambda location_val: location_values_filter(location_val[0], location_val[1]),
                            sorted_values)

    return next(ordered_values, (None, None))


def search(values, already_searched=None):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    if already_searched is None:
        already_searched = set()

    serial_grid = serialize_grid(values)

    if serial_grid in already_searched:
        return None

    already_searched = already_searched | set([serial_grid],)

    values = reduce_puzzle(values)
    if values is False:
        return False

    if sudoku_solved(values):
        return values

    cell, cell_values = get_location_with_least_values(values)

    # Now use recursion to solve each one of the resulting sudokus,
    # and if one returns a value (not False), return that answer!
    for potential_val in cell_values:
        new_values = values.copy()
        new_values[cell] = potential_val

        attempt = search(new_values, already_searched)
        if attempt and not contains_clashes(attempt):
            return attempt
        else:
            continue

if __name__ == '__main__':
    print('initial values\n')
    display(test_values)
    print('\nmy search\n')
    my_search = search(test_values.copy())
    display(my_search)
    print('\nideal search\n')
    ideal = ideal_search(test_values.copy())
    display(ideal)

    print("my search matches ideal: {}".format(my_search == ideal))