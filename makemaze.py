import random

print('hello world')
print('I\'m not sure what I\'m doing')
print('Well I think I am going to make a game...')
print('But we will see.')
print('As always IASWTFAY.')

#define your maze size and view size
def makemaze(x,y):

    if x < 2 or y < 2: return {('0','0'):[0,0,'']}

    #initiate the maze as a dictionary
    maze = dict()
    seed = random.randbytes(x*y)

    for i in range(x):
        for j in range(y):
            k = i*y + j
            if (seed[k] % 4 == 2 or seed[k] % 4 == 3) and (j != 0 and j != y-1):
                maze[str(i),str(j)] = maze.get((str(i),str(j)),[1,0,''])
            else:
                maze[str(i),str(j)] = maze.get((str(i),str(j)),[0,0,''])
            if seed[k] % 2 == 1 and (i != 0, i != x) and (i != 0 and i != x-1):
                maze[str(i),str(j)][1] = 1
    

    # The maze is made up of integers 0-3 where
    # 0 = no walls
    # 1 = _
    # 2 =  |
    # 3 = _|
    # The maze dictionary translates to
    # [1,0] =  |
    # [0,1] = _

    return maze