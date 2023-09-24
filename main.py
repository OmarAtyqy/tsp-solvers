from src.distances.distances import *
from src.solvers.grasp import GRASP
from src.solvers.tabu import Tabu

# define the cities coordinates and the distance function
cities = [
    (0, 0),
    (1, 5),
    (2, 3),
    (5, 2),
    (6, 5),
    (8, 3),
    (8, 1),
    (6, 0),
    (3, 0),
    (1, 1)
]
distance_function = euclidean_distance

# parameters for the GRASP solver
alpha = 0.5
max_iter = 100

# parameters for the Tabu solver
max_iterations = 100
tabu_tenure = 10


def main():

    # ============================= GRASP =============================

    # initialize the GRASP solver
    # grasp_solver = GRASP(
    #     cities=cities,
    #     alpha=alpha,
    #     max_iter=max_iter,
    #     distance=distance_function
    # )

    # solve the problem using the GRASP algorithm and get the solution
    # grasp_solver.solve()
    # grasp_solution, grasp_cost = grasp_solver.get_solution()

    # print the best solution and its cost
    # print('GRASP Solution: ', grasp_solution)
    # print('GRASP Cost: ', grasp_cost)

    # ============================= TABU =============================

    # initialize the Tabu solver
    tabu_solver = Tabu(
        coordinates=cities,
        max_iterations=max_iterations,
        tabu_tenure=tabu_tenure,
        distance_function=distance_function
    )

    # solve the problem using the Tabu Search algorithm and get the solution
    tabu_solver.solve()
    tabu_solution, tabu_cost = tabu_solver.get_solution()

    # print the best solution and its cost
    print('TABU Solution: ', tabu_solution)
    print('TABU Cost: ', tabu_cost)


if __name__ == '__main__':

    main()
