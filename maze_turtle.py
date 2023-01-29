from turtle import Screen, Turtle

# graphic object made to show elements in maze
class Square(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# function that creates new window with graphical implementation of given maze
def maze_in_turtle(size, maze):
    window = Screen()
    window.bgcolor("black")
    window.title("Maze")
    width = (size[1] * 24)+25
    height = (size[0] * 24)+25
    window.setup(width, height)
    window.tracer(0)

    wall,solution,p = Square(), Square(), Square()
    solution.color("red")      
    p.color("orange")

    for y in range(len(maze)):
            for x in range(len(maze[y])):
                # get turtle screen coordinates
                screen_x = (-(size[1]*12) + 10) + (x*24)
                screen_y = ((size[0]*12) - 10) - (y*24)

                character = maze[y][x]
                
                # pointing walls
                if character == 1:
                    wall.goto(screen_x, screen_y)
                    wall.stamp()
                
                # pointing solution path
                elif character == 2:
                    solution.goto(screen_x, screen_y)
                    solution.stamp()

                # pointing start and exit
                elif character in ['S', 'E'] :
                    p.goto(screen_x, screen_y)
                    p.stamp()

    return window