"""
function with implemented genetic algorithm:
rating maze and giving hints what can be changed in maze to make fitness score higher
"""
import pygad, numpy

def rate_maze(maze, solution_path):

    # set parameters to ga analysis
    walls = 0                # all walls (symbols 1 in maze)
    hor_walls = 0            # horizontal walls counter (2 square or longer)
    longest_hor_wall = 0     # longest horizontal wall
    hor_walls_3 = 0          # horizontal walls counter (3 to 5 squares)
    hor_walls_6 = 0          # horizontal walls counter (6 squares or longer)

    for line in maze:
        a=0
        for element in line:
                if element == 1:
                    walls += 1 
                    a+=1
                else:
                    if line != maze[0] or line != maze[0]: # eliminate top and bottom wall frame
                        if a==2:
                            hor_walls += 1
                        elif a>=3 and a<6:
                            hor_walls_3 += 1
                            hor_walls += 1
                        elif a>=6:
                            hor_walls_6 += 1
                            hor_walls += 1
                            if longest_hor_wall < a:
                                longest_hor_wall = a
                    a=0   

    # make weights for parameters
    function_inputs = [walls/(25*25), (len(solution_path)/100), (longest_hor_wall/8), 
                        (hor_walls/100), (hor_walls_3/100), (hor_walls_6/10)]
    
    desired_output = 0.6 + 0.55 + 0.8 + 0.7 + 0.32 + 0.4

    # design fitness functions (most basic one)
    def fitness_function(solution, solution_idx):
        output = numpy.sum(solution*function_inputs)
        fitness = 1.0 / numpy.abs(output - desired_output)
        return fitness
        
    ga_instance = pygad.GA(num_generations=50,
                        num_parents_mating=4,
                        fitness_func=fitness_function,
                        sol_per_pop=50,
                        num_genes=len(function_inputs),
                        init_range_low=-2,
                        init_range_high=5,
                        parent_selection_type="sss",
                        keep_parents=1,
                        crossover_type="single_point",
                        mutation_type="random",
                        mutation_percent_genes=10)
    ga_instance.run()


    # Results of ga analysis
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("\nFitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("\nWalls to cells:", walls/(25*25), "%")
    print("Maze solved in", len(solution_path), "steps")
    print("Longest horizontal wall:", longest_hor_wall)
    print("Number of horizontal walls:", hor_walls)
    print("Number of walls at least 3 units long:", hor_walls_3)
    print("Number of walls at least 6 units long:", hor_walls_6)
