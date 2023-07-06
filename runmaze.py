from makemaze import makemaze
from math import floor

def runmaze(x,y):

    # initialize the maze
    maze = makemaze(x,y)
    # set your starting spot to 0,0
    start = (0,0)
    blank = [1,1,'']
    check = [start]
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
            check.remove(mc)

    # place the goal near the center
    c = [floor(x/2),floor(y/2)]
    k1=1
    k2=1
    while k1<min(floor(x/2),floor(y/2)):
        for i in range(2):
            for j in range(k1):
                if maze[(c[0],c[1])][2]=='empty':
                        maze[(c[0],c[1])][2] = 'goal'
                        print(maze[(c[0],c[1])])
                        print(c)
                        return maze, (c[0],c[1])
                c[i] += k2
        k1+=1
        k2=k2*(-1)
    return maze, c