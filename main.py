# Description: Main file for the GRASP algorithm
from grasp import *

# main
if __name__ == "__main__":
    # data
    cities = [
        City("A", 1, 0),
        City("B", 2, 4),
        City("C", 7, 2),
        City("D", 0, 8),
        City("E", 6, 5),
        City("F", 1, 5),
        City("G", 3, 1),
        City("H", 0, 5)
    ]

    # test grasp using different values of alpha
    alphas = [i for i in range(1, 6)]
    iterations = 100
    explore_times = []
    exploit_times = []
    cost_solutions = []
    for alpha in alphas:
        h = []
        grasp = Grasp(alpha, iterations)
        best_solution, t_explore, t_exploit, h = grasp.search(cities)
        explore_times.append(t_explore)
        exploit_times.append(t_exploit)
        cost_solutions.append(best_solution.cost)
        print(f"Alpha: {alpha}")
        print(f"Explore time: {t_explore}")
        print(f"Exploit time: {t_exploit}")
        print()
        # plot the curve of the cost
        plt.figure(figsize=(5, 5))
        plt.plot(h)
        plt.title(f"impact of alpha on cost variation")
        plt.ylabel("Cost")
        plt.xlabel("Iteration")
        plt.savefig("{}{}.png".format("alpha_variation", alpha))
    # plot the results as group bars chart only for 2 variables (time explore and time exploit)
    plt.figure(figsize=(5, 5))
    barWidth = 0.25
    r1 = np.arange(len(explore_times))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, explore_times, color="blue", width=barWidth, label="Explore time")
    plt.bar(r2, exploit_times, color="red", width=barWidth, label="Exploit time")
    plt.xticks([r + barWidth for r in range(len(explore_times))], alphas)
    plt.title(f"impact of alpha on GRASP")
    plt.ylabel("Time")
    plt.xlabel("Alpha")
    plt.legend()
    plt.savefig("{}.png".format("alpha_time"))

    # plot the results of the cost
    plt.figure(figsize=(5, 5))
    plt.plot(alphas, cost_solutions)
    plt.title(f"impact of alpha on GRASP with {iterations} iterations")
    plt.ylabel("Cost")
    plt.xlabel("Alpha")
    plt.savefig("{}.png".format("alpha_cost"))

    # test grasp using different values of iterations
    alpha = 3
    iterations = [50, 100, 150, 200, 250]
    explore_times = []
    exploit_times = []
    cost_solutions = []
    for iteration in iterations:
        h = []
        grasp = Grasp(alpha, iteration)
        best_solution, t_explore, t_exploit, h = grasp.search(cities)
        explore_times.append(t_explore)
        exploit_times.append(t_exploit)
        cost_solutions.append(best_solution.cost)
        h.append(best_solution.cost)
        print(f"Iteration: {iteration}")
        print(f"Explore time: {t_explore}")
        print(f"Exploit time: {t_exploit}")
        print()
        # plot the curve of the cost
        plt.figure(figsize=(5, 5))
        plt.plot(h)
        plt.title(f"impact of iteration on cost variation")
        plt.ylabel("Cost")
        plt.xlabel("Iteration")
        plt.savefig("{}{}.png".format("iteration_variation", iteration))
    # plot the results as group bars chart only for 2 variables (time explore and time exploit)
    plt.figure(figsize=(5, 5))
    barWidth = 0.25
    r1 = np.arange(len(explore_times))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, explore_times, color="blue", width=barWidth, label="Explore time")
    plt.bar(r2, exploit_times, color="red", width=barWidth, label="Exploit time")
    plt.xticks([r + barWidth for r in range(len(explore_times))], iterations)
    plt.title(f"impact of iteration on GRASP")
    plt.ylabel("Time")
    plt.xlabel("Iteration")
    plt.legend()
    # save the plot
    plt.savefig("{}.png".format("iteration_time"))

    # plot the results of the cost
    plt.figure(figsize=(5, 5))
    plt.plot(iterations, cost_solutions)
    plt.title(f"impact of iteration on GRASP")
    plt.ylabel("Cost")
    plt.xlabel("Iteration")
    plt.savefig("{}.png".format("iteration_cost"))

    # generate random cities
    tasks = []
    for i in range(3):
        citie = []
        for j in range(10 * (i + 1)):
            citie.append(City(f"{i}{j}", random.randint(0, 30), random.randint(0, 30)))
        tasks.append(citie)          

    alpha = 3
    iteration = 100
    explore_times = []
    exploit_times = []
    cost_solutions = []
    for citie in tasks:
        h = []
        grasp = Grasp(alpha, iteration)
        best_solution, t_explore, t_exploit, h = grasp.search(citie)
        explore_times.append(t_explore)
        exploit_times.append(t_exploit)
        cost_solutions.append(best_solution.cost)
        h.append(best_solution.cost)
        print(f"Nbr Cities: {len(citie)}")
        print(f"Explore time: {t_explore}")
        print(f"Exploit time: {t_exploit}")
        print()
        # plot the curve of the cost
        plt.figure(figsize=(5, 5))
        plt.plot(h)
        plt.title(f"impact of number of cities on cost variation")
        plt.ylabel("Cost")
        plt.xlabel("cities")
        plt.savefig("{}{}.png".format("cities_variation", len(citie)))
        # print the solution
        best_solution.plot_solution(best_solution)
    # plot the results as group bars chart only for 2 variables (time explore and time exploit)
    plt.figure(figsize=(5, 5))
    barWidth = 0.25
    r1 = np.arange(len(explore_times))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, explore_times, color="blue", width=barWidth, label="Explore time")
    plt.bar(r2, exploit_times, color="red", width=barWidth, label="Exploit time")
    plt.xticks([r + barWidth for r in range(len(explore_times))], [10, 20, 30])
    plt.title(f"impact of number of cities on GRASP")
    plt.ylabel("Time")
    plt.xlabel("cities")
    plt.legend()
    # save the plot
    plt.savefig("{}.png".format("cities_time"))

    # plot the results of the cost
    plt.figure(figsize=(5, 5))
    plt.plot([10, 20, 30], cost_solutions)
    plt.title(f"impact of number of cities on GRASP")
    plt.ylabel("Cost")
    plt.xlabel("cities")
    plt.savefig("{}.png".format("cities_cost"))