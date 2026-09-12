"""Exercise 5 sample solution."""

import math


def distance_to_origin(x_coordinate, y_coordinate):
    """ returns the distance from (0, 0) to (x_coordinate, y_coordinate) """
    return math.sqrt(x_coordinate ** 2 + y_coordinate ** 2)
