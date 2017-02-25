from collections import Counter
from utils import *

test_values = {
    'A3': '3',
     'H8': '1467',
     'A2': '4578',
     'A4': '49',
     'D5': '3456',
     'F3': '6',
     'G2': '1347',
     'B9': '1',
     'D3': '8',
     'I3': '5',
     'I1': '46',
     'E5': '34569',
     'H1': '8',
     'E3': '49',
     'I2': '4679',
     'H4': '2',
     'B2': '24678',
     'C7': '4',
     'F9': '345',
     'A5': '2',
     'I5': '1',
     'F8': '1345',
     'F6': '8',
     'D8': '34567',
     'B4': '3',
     'G1': '134',
     'C8': '23579',
     'D2': '345',
     'A7': '6',
     'G5': '478',
     'E1': '7',
     'H5': '457',
     'A1': '45',
     'D6': '2',
     'G8': '1478',
     'G3': '2',
     'G7': '5',
     'F4': '7',
     'I4': '4',
     'I9': '2467',
     'D1': '345',
     'G4': '6',
     'B5': '47',
     'D7': '9',
     'G9': '47',
     'E7': '1',
     'C9': '2357',
     'F1': '1345',
     'B8': '278',
     'I6': '47',
     'E6': '4',
     'H6': '3',
     'H9': '9',
     'C2': '257',
     'B3': '47',
     'E2': '123459',
     'C4': '8',
     'D4': '1',
     'E8': '13456',
     'B1': '9',
     'I8': '24678',
     'H7': '17',
     'B6': '5',
     'A6': '1',
     'I7': '3',
     'A8': '5789',
     'E9': '8',
     'C3': '1',
     'C1': '25',
     'F2': '13459',
     'A9': '57',
     'F5': '3459',
     'C5': '79',
     'G6': '9',
     'E4': '459',
     'D9': '34567',
     'F7': '2',
     'H2': '1467',
     'H3': '47',
     'C6': '6',
     'B7': '78'
}


def get_mini_grid_locations(location):
    for grid in square_units:
        if location in grid:
            # grid_peers = grid.copy()
            # # grid_peers.pop(grid_peers.index(location))
            # return grid_peers
            return grid


def get_mini_grid_dict(location, values):
    mini_grid_locations = get_mini_grid_locations(location)

    return {other_location: values[other_location] for other_location in mini_grid_locations}


def get_unsolved_values(values):
    return {k: v for k, v in values.items() if len(v) > 1}


def get_peer_locations(location):
    col_peers = [location[0] + str(x) for x in cols if location[0] + str(x) != location]
    row_peers = [str(x) + location[1] for x in rows if str(x) + location[1] != location]
    for grid in square_units:
        if location in grid:
            grid_peers = [x for x in grid if x != location]
            break

    for l in chain(col_peers, row_peers, grid_peers):
        yield l


def old_only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    # display(values)
    for unit in unitlist:

        unit_dict = {cell: values[cell] for cell in unit}
        unsolved_values = unit_dict # get_unsolved_values(unit_dict)
        while True:
            unit_values = unsolved_values.values()
            unit_potential_vals = Counter(list(chain(*unit_values)))
            single_values = [number for number, count in unit_potential_vals.items() if count == 1]
            # if single_values:

            eliminated = 0
            for val in single_values:
                for cell, potential_vals in unsolved_values.items():
                    if val in potential_vals:
                        values[cell] = val
                        unit_dict[cell] = val

                        print('\n')
                        print(cell, val)
                        display(values)
                        # import pdb; pdb.set_trace()
                        for other_cell in get_peer_locations(cell):
                            if len(values[other_cell]) > 1:
                                values[other_cell] = values[other_cell].replace(val, '')
                                if other_cell in unit_dict:
                                    unit_dict[other_cell] = unit_dict[other_cell].replace(val, '')

                    elif len(potential_vals) == 1:
                        eliminated += 1

            if len(single_values) == 0 and eliminated == 0:
                break
            unsolved_values = get_unsolved_values({cell: values[cell] for cell in unit})

    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form aft13456er filling in only choices.
    """
    for unit in unitlist:

        for cell in unit:
            unit_dict = {cell: values[cell] for cell in unit}
            unsolved_values = unit_dict # get_unsolved_values(unit_dict)
            if cell not in unsolved_values:
                continue
            num_occurences = Counter(chain(*unsolved_values.values()))
            single_occurences = [val for val, occurence in num_occurences.items() if occurence == 1]
            if len(single_occurences) == 0:
                continue

            cell_vals = values[cell]
            for val in single_occurences:
                if val in cell_vals:
                    values[cell] = val
                    break

    return values


def ideal_soln(values):
    """
    taken from udacity cource, used to compare personal soln to ideal
    Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


if __name__ == '__main__':
    display(test_values)
    print('\n')
    only_choice_values_dict = only_choice(test_values.copy())
    print('\n')
    display(only_choice_values_dict)
    print('\n')
    ideal = ideal_soln(test_values.copy())
    display(ideal)
    # display(test_values)

