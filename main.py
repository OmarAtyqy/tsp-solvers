from src.solver.grasp import GRASP
import numpy as np


# define the cities to visit
cities = np.array([
    [0, 0],
    [1, 5],
    [2, 3],
    [5, 2],
    [6, 4],
    [7, 1],
    [8, 6],
    [9, 0],
    [10, 5],
    [11, 3],
    [14, 2]
])


def main():

    # initialize the GRASP solver
    solver = GRASP(cities, alpha=0.5, max_iter=100)

    # solve the TSP
    solver.solve()

    # print the best solution found
    print('Best solution found:')
    print(solver.best_solution)
    print('Cost: {}'.format(solver.best_cost))


if __name__ == '__main__':

    main()
