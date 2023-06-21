import random
import time
from numpy import array
import sys
print('hello world')
print('I\'m not sure what I\'m doing')
print('Well I think I am going to make a game...')
print('But we will see.')
print('As always IASWTFAY.')


#define your maze size and view size
def makemaze(x_maze,y_maze):
    #x_maze = 100
    #y_maze = 100


    maze = array([[0]*y_maze]*x_maze)
    print(maze[0, 0])

    seed = random.randbytes((x_maze)*(y_maze))
    #print(len(seed))
    #print('printing seed')
    #print(seed)

    k=0
    for i in range(x_maze):
        for j in range(y_maze):
            maze[i,j] = int(seed[(i*y_maze)+j])

    # The maze is made up of integers 0-3 where
    # 0 = no walls
    # 1 = _
    # 2 =  |
    # 3 = _|

    # Condition the maze so that nothing interferes with
    # transiting the borders of the maze
    for i in range(x_maze):
        if maze[i,0] % 4 == 2 or maze[i,0] % 4 == 3:
            maze[i,0] = maze[i,0] - 2
        maze[i,y_maze-1] = 0
    for j in range(y_maze):
        if maze[0,j] % 2 == 1:
            maze[0,j] = maze[0,j] - 1
        maze[x_maze-1,j] = 0

    # make a projection of the maze
    #maze_pj = array([[0]*x_maze]*y_maze)
    #for i in range(x_maze):
    #    for j in range(y_maze):
    #        maze_pj[i,j] = maze[i,j] % 4

    return maze