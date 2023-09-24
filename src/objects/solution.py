"""
This module implements the Solution class.
"""

import numpy as np


class Solution:

    def __init__(self, cities, distance):
        self.cities = cities
        self.distance = distance

        self.cost = self._calculate_cost()

    def _calculate_cost(self):
        """
        This method calculates the cost of the solution.
        """
        return np.sum([self.distance(self.cities[i], self.cities[i+1]) for i in range(len(self.cities)-1)])
