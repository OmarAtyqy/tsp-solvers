"""
This module implements mutliple distance functions.
"""

import numpy as np


def euclidean_distance(city_a, city_b):
    """
    This function calculates the Euclidean distance between two cities.
    """
    return np.linalg.norm(city_a - city_b)
