from makemaze import makemaze
from math import floor

def runmaze(x,y):

    # initialize the maze
    maze = makemaze(x,y)
    # set your starting spot to 0,0
    start = (0,0)
    blank = [1,1,'']
    check = [start]
    check_all = [start]
    maze[start][2] = 'empty'

    # check to see which spaces are achievable
    while check != []:
        for mc in check:
            # check up
            maze_local = [[(mc[0],mc[1]-1),1],
                          [(mc[0]+1,mc[1]),0],
                          [(mc[0],mc[1]+1),1],
                          [(mc[0]-1,mc[1]),0]]

            for ml in maze_local:
                if maze.get(ml[0],'') != '' and maze.get(ml[0],blank)[ml[1]] == 0 and maze.get(ml[0],blank)[2] != 'empty':
                    maze[ml[0]][2] = 'empty'
                    check.append(ml[0])
                    check_all.append(ml[0])
            check.remove(mc)

    check_all.sort()
    goal = check_all[floor(len(check_all)/2)]
    maze[goal][2] = 'goal'
    return maze, goal