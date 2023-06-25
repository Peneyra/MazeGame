from makemaze import makemaze
from time import time
from printmaze import printmaze

# give dimensions of the maze
x = 100
y = 100

t = time()

# initialize the maze
maze = makemaze(x,y)
# set your starting spot to 0,0
start = ('0','0')
blank = [1,1,'']
check = [start]
maze[start][2] = 'empty'

# check to see which spaces are achievable
while check != []:
    for mc in check:
        #print(s)
        #print(maze[s[0],s[1]])
        # check up
        c = [int(mc[0]),int(mc[1])]
        [mu,mr,md,ml] = [(str(c[0]),str(c[1]-1)),(str(c[0]+1),str(c[1])),(str(c[0]),str(c[1]+1)),(str(c[0]-1),str(c[1]))]

        if maze.get(mu,'') != '' and maze.get(mu,blank)[1] == 0 and maze.get(mu,blank)[2] != 'empty':
            maze[mu][2] = 'empty'
            check.append(mu)
        if maze.get(mr,'') != '' and maze.get(mc,blank)[0] == 0 and maze.get(mr,blank)[2] != 'empty':
            maze[mr][2] = 'empty'
            check.append(mr)
        if maze.get(md,'') != '' and maze.get(mc,blank)[1] == 0 and maze.get(md,blank)[2] != 'empty':
            maze[md][2] = 'empty'
            check.append(md)
        if maze.get(ml,'') != '' and maze.get(ml,blank)[0] == 0 and maze.get(ml,blank)[2] != 'empty':
            maze[ml][2] = 'empty'
            check.append(ml)
        check.remove(mc)

#print(spaces_good)
print(time() - t)
printmaze(maze,x,y)