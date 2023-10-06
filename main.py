from src.distances.distances import *
from src.solvers.grasp import GRASP
from src.solvers.tabu import Tabu
import matplotlib.pyplot as plt
import random
import tqdm

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
    
    # evaluate how the tabu tenure affects the algorithm performance
    
    list_tabu_tenure = [1, 2, 5, 10, 15, 20]
    list_tabu_cost = []
    list_tabu_time_explore = []
    list_tabu_time_exploit = []
    for tabu_tn in tqdm.tqdm(list_tabu_tenure, desc='Tabu Tenure', unit='tenure'):
        tabu_solver.tabu_tenure = tabu_tn
        # solve the problem using the Tabu algorithm and get the solution
        explore_time, exploit_time = tabu_solver.solve()
        tabu_solution, tabu_cost = tabu_solver.get_solution()
        list_tabu_cost.append(tabu_cost)
        list_tabu_time_explore.append(explore_time)
        list_tabu_time_exploit.append(exploit_time)

    # plot the results in group bar chart for time explore and exploit
    fig, ax = plt.subplots()
    index = np.arange(len(list_tabu_tenure))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, list_tabu_time_explore, bar_width,
    alpha=opacity,
    color='b',
    label='Time Explore')

    rects2 = plt.bar(index + bar_width, list_tabu_time_exploit, bar_width,
    alpha=opacity,
    color='g',
    label='Time Exploit')

    plt.xlabel('Tabu Tenure')
    plt.ylabel('Time')
    plt.title('Time Explore and Exploit')
    plt.xticks(index + bar_width, list_tabu_tenure)
    plt.legend()

    plt.tight_layout()
    plt.savefig('time_tabu_tenure.png')

    # plot the results in line chart for cost
    fig, ax = plt.subplots()
    plt.plot(list_tabu_tenure, list_tabu_cost, marker='o')
    plt.xlabel('Tabu Tenure')
    plt.ylabel('Cost')
    plt.title('Cost')
    plt.savefig('cost_tabu_tenure.png')
    
    # evaluate how the number of cities affects the algorithm performance
    list_cities = [10, 20, 30]
    list_cities_cost = []
    list_cities_time_explore = []
    list_cities_time_exploit = []
    
    for n in tqdm.tqdm(list_cities, desc='Cities', unit='cities'):
        # define the cities coordinates and the distance function
        c = []
        for i in range(n):
            c.append((random.randint(0, 100), random.randint(0, 100)))
        # initialize the Tabu solver
        tabu_solver = Tabu(
            coordinates=c,
            max_iterations=max_iterations,
            tabu_tenure=tabu_tenure,
            distance_function=distance_function
        )
        # solve the problem using the Tabu algorithm and get the solution
        explore_time, exploit_time = tabu_solver.solve()
        tabu_solution, tabu_cost = tabu_solver.get_solution()
        list_cities_cost.append(tabu_cost)
        list_cities_time_explore.append(explore_time)
        list_cities_time_exploit.append(exploit_time)

    # plot the results in group bar chart for time explore and exploit
    fig, ax = plt.subplots()
    index = np.arange(len(list_cities))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, list_cities_time_explore, bar_width,
    alpha=opacity,
    color='b',
    label='Time Explore')

    rects2 = plt.bar(index + bar_width, list_cities_time_exploit, bar_width,
    alpha=opacity,
    color='g',
    label='Time Exploit')

    plt.xlabel('Number of Cities')
    plt.ylabel('Time')
    plt.title('Time Explore and Exploit')
    plt.xticks(index + bar_width, list_cities)
    plt.legend()

    plt.tight_layout()
    plt.savefig('time_cities.png')

    # plot the results in line chart for cost
    fig, ax = plt.subplots()
    plt.plot(list_cities, list_cities_cost, marker='o')
    plt.xlabel('Number of Cities')
    plt.ylabel('Cost')
    plt.title('Cost')
    plt.savefig('cost_cities.png')

    
if __name__ == '__main__':
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
    main()