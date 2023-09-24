"""
This module implements mutliple distance functions.
"""

import numpy as np


def euclidean_distance(city_a, city_b):
    """
    This function calculates the Euclidean distance between two cities.
    :param city_a: tuple containing the coordinates of city A
    :param city_b: tuple containing the coordinates of city B
    """
    return np.linalg.norm(np.array(city_a) - np.array(city_b))
