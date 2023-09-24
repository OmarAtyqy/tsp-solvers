"""
This module implements the Tabu Search algorithm for solving the Traveling Salesman Problem.
"""

import copy

import numpy as np

from src.distances.distances import euclidean_distance


class Tabu:
    def __init__(self, coordinates, max_iterations, tabu_tenure, distance_function=euclidean_distance):
        self.coordinates = coordinates
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.distance_function = distance_function

        # initialize the solution and cost and the distance matrix
        self.distance_matrix = self.calculate_distance_matrix()
        self.best_solution = None
        self.best_cost = float('inf')

    def calculate_distance_matrix(self):
        n = len(self.coordinates)
        distance_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = self.distance_function(
                    self.coordinates[i], self.coordinates[j])
        return distance_matrix

    def calculate_total_distance(self, tour):
        total_distance = 0
        n = len(tour)
        for i in range(n):
            total_distance += self.distance_matrix[tour[i - 1], tour[i]]
        return total_distance

    def generate_neighbors(self, solution):
        neighbors = []
        n = len(solution)
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = np.copy(solution)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def solve(self):
        n = len(self.distance_matrix)

        # Initialize current and best solutions
        current_solution = np.random.permutation(n)
        best_solution = copy.deepcopy(current_solution)
        best_cost = self.calculate_total_distance(best_solution)

        # Initialize tabu list
        tabu_list = []

        for _ in range(self.max_iterations):
            # Generate neighboring solutions (swap two cities)
            neighbors = self.generate_neighbors(current_solution)

            # Evaluate neighbors and select the best non-tabu neighbor
            best_neighbor = None
            best_neighbor_cost = float('inf')
            for neighbor in neighbors:
                neighbor_cost = self.calculate_total_distance(neighbor)
                if tuple(neighbor) not in tabu_list and neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost

            # Update current solution
            current_solution = best_neighbor

            # Update tabu list
            tabu_list.append(tuple(best_neighbor))
            if len(tabu_list) > self.tabu_tenure:
                tabu_list.pop(0)

            # Update the best solution if needed
            if best_neighbor_cost < best_cost:
                best_solution = best_neighbor
                best_cost = best_neighbor_cost

        # Convert solution to list of tuples (corresponding to city order)
        best_solution_order = [self.coordinates[i] for i in best_solution]

        # Update the best solution and cost
        self.best_solution = best_solution_order
        self.best_cost = best_cost

    def get_solution(self):
        return self.best_solution, self.best_cost
