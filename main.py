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
        City("H", 0, 5),#
        # City("I", 5, 2),
        # City("J", 3, 8),
        # City("K", 8, 0),
        # City("L", 5, 6),
        # City("M", 2, 3),
        # City("N", 4, 7),
        # City("O", 6, 3),
        # City("P", 4, 1),
        # City("Q", 7, 8),
        # City("R", 1, 1),
        # City("S", 3, 4),
        # City("T", 8, 4),
        # City("U", 4, 0),
        # City("V", 2, 8),
        # City("W", 6, 7),
        # City("X", 0, 2),
        # City("Y", 5, 0),
        # City("Z", 7, 5),
    ]

    # alpha = 3
    # iterations = 100

    # search
    # grasp = Grasp(alpha, iterations)
    # best_solution, t_explore, t_exploit = grasp.search(cities)
    # best_solution.print_solution(best_solution)
    # best_solution.plot_solution(best_solution)

    # test grasp using different values of alpha
    alphas = [i for i in range(1, 6)]
    iterations = 50
    explore_times = []
    exploit_times = []
    cost_solutions = []
    for alpha in alphas:
        grasp = Grasp(alpha, iterations)
        best_solution, t_explore, t_exploit = grasp.search(cities)
        explore_times.append(t_explore)
        exploit_times.append(t_exploit)
        cost_solutions.append(best_solution.cost)
        print(f"Alpha: {alpha}")
        print(f"Explore time: {t_explore}")
        print(f"Exploit time: {t_exploit}")
        print()
    # plot the results as group bars chart only for 2 variables (time explore and time exploit)
    plt.figure(figsize=(5, 5))
    barWidth = 0.25
    r1 = np.arange(len(explore_times))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, explore_times, color="blue", width=barWidth, label="Explore time")
    plt.bar(r2, exploit_times, color="red", width=barWidth, label="Exploit time")
    plt.xticks([r + barWidth for r in range(len(explore_times))], alphas)
    plt.title(f"impact of alpha on GRASP with {iterations} iterations")
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
        grasp = Grasp(alpha, iteration)
        best_solution, t_explore, t_exploit = grasp.search(cities)
        explore_times.append(t_explore)
        exploit_times.append(t_exploit)
        cost_solutions.append(best_solution.cost)
        print(f"Iteration: {iteration}")
        print(f"Explore time: {t_explore}")
        print(f"Exploit time: {t_exploit}")
        print()
    # plot the results as group bars chart only for 2 variables (time explore and time exploit)
    plt.figure(figsize=(5, 5))
    barWidth = 0.25
    r1 = np.arange(len(explore_times))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, explore_times, color="blue", width=barWidth, label="Explore time")
    plt.bar(r2, exploit_times, color="red", width=barWidth, label="Exploit time")
    plt.xticks([r + barWidth for r in range(len(explore_times))], alphas)
    plt.title(f"impact of iteration on GRASP with alpha = {alpha}")
    plt.ylabel("Time")
    plt.xlabel("Iteration")
    plt.legend()
    # save the plot
    plt.savefig("{}.png".format("iteration_time"))

    # plot the results of the cost
    plt.figure(figsize=(5, 5))
    plt.plot(alphas, cost_solutions)
    plt.title(f"impact of iteration on GRASP with alpha = {alpha}")
    plt.ylabel("Cost")
    plt.xlabel("Iteration")
    plt.savefig("{}.png".format("iteration_cost"))
