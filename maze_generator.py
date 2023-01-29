"""
Function that creates random maze with only 1 way from start to exit
"""
from random import choice

def maze_generator(maze_size):
	
	height=maze_size[0]
	width=maze_size[1]

	wall_symbol = 1
	cell_symbol = 0
	unvisited_symbol = 'u'

	maze, walls = [], []

	# mark all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited_symbol)
		maze.append(line)

	# randomize initial point and set it a cell
	initial_height = choice(range(1, height-2))
	initial_width = choice(range(1, width-2))
	maze[initial_height][initial_width] = cell_symbol

	# mark walls around initial cell 
	maze[initial_height-1][initial_width] = wall_symbol
	maze[initial_height][initial_width - 1] = wall_symbol
	maze[initial_height][initial_width + 1] = wall_symbol
	maze[initial_height + 1][initial_width] = wall_symbol

	# add walls around initial cell to wall list
	walls.append([initial_height - 1, initial_width])
	walls.append([initial_height + 1, initial_width])
	walls.append([initial_height, initial_width - 1])
	walls.append([initial_height, initial_width + 1])

	# return number of cells around wall
	def surroundingCells(maze, wall, cell_symbol):
		counter = 0
		if (maze[wall[0]-1][wall[1]] == cell_symbol):
			counter += 1
		if (maze[wall[0]+1][wall[1]] == cell_symbol):
			counter += 1
		if (maze[wall[0]][wall[1]-1] == cell_symbol):
			counter +=1
		if (maze[wall[0]][wall[1]+1] == cell_symbol):
			counter += 1
		return counter

	# loop (building process of subsequent paths and walls)
	while (walls):
		wall = walls[(choice(range(0, len(walls))))]

		# check if chosen wall is not left border wall
		if (wall[1] != 0):
			if (maze[wall[0]][wall[1]-1] == unvisited_symbol and maze[wall[0]][wall[1]+1] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on top cell
					if (wall[0] != 0):
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):	
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])


		# check if chosen wall is not top border wall
		if (wall[0] != 0):
			if (maze[wall[0]-1][wall[1]] == unvisited_symbol and maze[wall[0]+1][wall[1]] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on top cell
					if (wall[0] != 0):
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

		# check if chosen wall is not bottom border wall
		if (wall[0] != height-1):
			if (maze[wall[0]+1][wall[1]] == unvisited_symbol and maze[wall[0]-1][wall[1]] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

		# check if chosen wall is not right border wall
		if (wall[1] != width-1):
			if (maze[wall[0]][wall[1]+1] == unvisited_symbol and maze[wall[0]][wall[1]-1] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

					# make wall on top cell
					if (wall[0] != 0):	
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

		# remove wall from list of walls
		for w in walls:
			if (w[0] == wall[0] and w[1] == wall[1]):
				walls.remove(w)
		
	# mark remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == unvisited_symbol):
				maze[i][j] = wall_symbol

	# mark player starting position
	for i in range(0, width):
		if (maze[1][i] == cell_symbol):
			maze[1][i] = 'S'
			player_position = [1, i]
			break

	# mark level exit position
	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == cell_symbol):
			maze[height-2][i] = 'E'
			break

	return maze