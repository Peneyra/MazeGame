import random

print('hello world')
print('I\'m not sure what I\'m doing')
print('Well I think I am going to make a game...')
print('But we will see.')
print('As always IASWTFAY.')

# Each space will be represented by ('0','0')
# define your maze size and view size
def makemaze(x,y):

    if x < 2 or y < 2: return {(0,0):[0,0,'']}

    #initiate the maze as a dictionary
    maze = dict()
    seed = random.randbytes(x*y)

    for i in range(x-1):
        for j in range(y-1):
            k = i*y + j
            if (seed[k] % 4 == 2 or seed[k] % 4 == 3) and j > 0:
                maze[(i,j)] = maze.get((i,j),[1,0,''])
            else:
                maze[(i,j)] = maze.get((i,j),[0,0,''])
            if seed[k] % 2 == 1 and i > 0 :
                maze[(i,j)][1] = 1
    

    # The maze is made up of integers 0-3 where
    # 0 = no walls
    # 1 = _
    # 2 =  |
    # 3 = _|
    # The maze dictionary translates to
    # [1,0] =  |
    # [0,1] = _

    return maze