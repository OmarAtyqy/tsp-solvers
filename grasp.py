# implements the greedy randomized adaptive search procedure (GRASP) for the
# traveling salesman problem (TSP)

import random
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import time

# class city
class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


# class solution
class Solution:
    def __init__(self, cities):
        self.cities = cities
        self.cost = self.calculate_cost()

    # calculate the cost of the solution
    def calculate_cost(self):
        cost = 0
        for i in range(len(self.cities) - 1):
            cost += np.sqrt(
                (self.cities[i].x - self.cities[i + 1].x) ** 2
                + (self.cities[i].y - self.cities[i + 1].y) ** 2
            )
        return cost

    # print the solution
    def __repr__(self):
        return f"Solution: {self.cities} with cost {self.cost}"

    def print_solution(self, solution):
        for city in solution.cities:
            print(city.name, end=" ")
        print(f"with cost {solution.cost}")

    # plot the solution
    def plot_solution(self, solution):
        plt.figure(figsize=(5, 5))
        plt.scatter(
            [city.x for city in solution.cities],
            [city.y for city in solution.cities],
            color="red",
        )
        for city in solution.cities:
            plt.annotate(city.name, (city.x, city.y))
        # plot the path
        for i in range(len(solution.cities) - 1):
            plt.plot(
                [solution.cities[i].x, solution.cities[i + 1].x],
                [solution.cities[i].y, solution.cities[i + 1].y],
                color="blue",
            )
        plt.plot(
            [solution.cities[-1].x, solution.cities[0].x],
            [solution.cities[-1].y, solution.cities[0].y],
            color="blue",
        )
        plt.show()


# class grasp
class Grasp:
    def __init__(self, alpha, iterations):
        self.alpha = alpha
        self.iterations = iterations

    def sort_by_cost(self, solutions):
        return sorted(solutions, key=lambda x: x.cost)

    def two_opt(self, solution, i, j):
        """
        2-opt swap: swap two cities in the solution
        """
        new_solution = solution.cities.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        return Solution(new_solution)

    def local_search(self, solution):
        """
        local search: 2-opt
        """
        while True:
            best_solution = solution
            for i in range(len(solution.cities) - 1):
                for j in range(i + 1, len(solution.cities)):
                    new_solution = self.two_opt(solution, i, j)
                    if new_solution.cost < best_solution.cost:
                        best_solution = new_solution
            if best_solution == solution:
                return best_solution
            solution = best_solution

    def construct_greedy_randomized_solution(self, cities):
        """
        construct a greedy randomized solution
        args:
            cities: list of cities
        returns:
            solution: a solution
        """
        solution = Solution([cities[0]])
        cities = cities[1:]
        while cities:
            rcl = []
            for city in cities:
                cost = np.sqrt(
                    (city.x - solution.cities[-1].x) ** 2
                    + (city.y - solution.cities[-1].y) ** 2
                )
                rcl.append((city, cost))
            rcl = sorted(rcl, key=lambda x: x[1])[: self.alpha]
            chosen_city = random.choice(rcl)[0]
            solution.cities.append(chosen_city)
            cities.remove(chosen_city)
        solution.cost = solution.calculate_cost()
        return solution

    def search(self, cities):
        """
        search: main function
        args:
            cities: list of cities
        returns:
            best_solution: the best solution found
        """
        solutions = []
        exploration_time = 0
        exploitation_time = 0
        for i in tqdm.tqdm(range(self.iterations)):
            start = time.time()
            solution = self.construct_greedy_randomized_solution(cities)
            end = time.time()
            exploration_time += end - start
            start = time.time()
            solution = self.local_search(solution)
            end = time.time()
            exploitation_time += end - start
            solutions.append(solution)
        return self.sort_by_cost(solutions)[0], exploration_time, exploitation_time
