from maze_generator import maze_generator
from maze_solver import maze_solver
from maze_ga import rate_maze
from maze_turtle import  maze_in_turtle

# initializing data and creating maze
size= [25, 25]
generate_maze = maze_generator(size)

# getting solved maze and shortest solution path from start to exit
maze, solution_path = maze_solver(generate_maze)

# rating maze using genetic algorithm
rate_maze(maze, solution_path)

# load turtle window with implemented maze
window = maze_in_turtle(size, maze)

# infinite loop to show turtle window with graphical implementation of maze
while True:
	window.update()
