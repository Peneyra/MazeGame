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
spaces_good = [[0,0]]
spaces_check = [[0,0]]

# append both spaces_check and spaces_good
def appen(a,b,c,d):
    c.append([a,b])
    d.append([a,b])

# check to see which spaces are achievable
while spaces_check != []:
    for s in spaces_check:
        #print(s)
        #print(maze[s[0],s[1]])
        # check up
        [a,b] = [s[0],s[1]]
        if b > 0:
            if maze[a,b-1] % 2 != 1 and [a,b-1] not in spaces_good: appen(a,b-1,spaces_check,spaces_good)
        if a > 0:
            if maze[a-1,b] % 4 != 2 and maze[a-1,b] % 4 != 3 and [a-1,b] not in spaces_good: appen(a-1,b,spaces_check,spaces_good)
        if b < y-1:
            if maze[a,b] % 2 != 1 and [a,b+1] not in spaces_good: appen(a,b+1,spaces_check,spaces_good)
        if a < x-1:
            if maze[a,b] % 4 != 2 and maze[a,b] % 4 != 3 and [a+1,b] not in spaces_good: appen(a+1,b,spaces_check,spaces_good)
        spaces_check.remove(s)

#print(spaces_good)
print(time() - t)
printmaze(maze,spaces_good)