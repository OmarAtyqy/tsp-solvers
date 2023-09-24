"""
This module implements the GRASP algorithm for solving the Traveling Salesman Problem.
"""

import numpy as np

from src.distances.distances import *
from src.objects.solution import Solution


class GRASP:

    def __init__(self, cities, alpha, max_iter, distance=euclidean_distance):
        self.cities = cities
        self.alpha = alpha
        self.max_iter = max_iter
        self.distance = distance

        # initialize the solver
        self.best_solution = None
        self.best_cost = float('inf')

    def solve(self):
        """
        This method solves the TSP using the GRASP algorithm.
        """

        for _ in range(self.max_iter):

            solution = self._construct_randomized_greedy_solution()
            solution = self._local_search(solution)

            if solution.cost < self.best_cost:
                self.best_cost = solution.cost
                self.best_solution = solution

    def _construct_randomized_greedy_solution(self):
        pass

    def _sort_by_cost(self, candidate_list):
        pass

    def _local_search(self, solution):
        pass

    def _two_opt(self, solution):
        pass
