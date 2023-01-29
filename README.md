# Random maze
Python program, that generates random maze (as list of lists) with solution and gives hints what can be changed to make maze more interesting. 

Required libraries to run this project: pygad, turtle, numpy, random.

# Main steps
1. Generating random maze that has only one path from start to end
2. Using maze solving function to get path from start to end in current maze
3. Implementing genetic algorithm with chosen parameters of current maze
4. Graphical presentation of maze with solution path
5. Analysis of genetic algorithms work

# Example of maze
This example of maze made by this program is obviously one of many possibilites

![maze-example](https://user-images.githubusercontent.com/123515299/215359005-2b65964f-67c4-45e2-9932-5ad1778b1dd5.png)
# Example of genetic algorithm output
![ga-example](https://user-images.githubusercontent.com/123515299/215359043-a26357f6-bad1-4950-be54-b0227b758f58.png)

Hints given by GA to improve current maze:
1. Make the solution path longer
2. Shorten the longest horizontal wall
3. Reduce total number of 6 or more square walls
