from makemaze import makemaze
from time import time

# give dimensions of the maze
x = 100
y = 100

t = time()
# initialize the maze
maze = makemaze(x,y)
spaces_good = [[0,0]]
spaces_check = [[0,0]]
while spaces_check != []:
    for s in spaces_check:
        #print(s)
        #print(maze[s[0],s[1]])
        # check up
        if s[1] > 0:
            if maze[s[0],s[1]-1] % 2 != 1 and [s[0],s[1]-1] not in spaces_good:
                spaces_check.append([s[0],s[1]-1])
                spaces_good.append([s[0],s[1]-1])
        if s[0] > 0:
            if maze[s[0]-1,s[1]] % 4 != 2 and maze[s[0]-1,s[1]] % 4 != 3 and [s[0]-1,s[1]] not in spaces_good:
                spaces_check.append([s[0]-1,s[1]])
                spaces_good.append([s[0]-1,s[1]])
        if s[1] < y-1:
            if maze[s[0],s[1]] % 2 != 1 and [s[0],s[1]+1] not in spaces_good:
                spaces_check.append([s[0],s[1]+1])
                spaces_good.append([s[0],s[1]+1])
        if s[0] < x-1:
            if maze[s[0],s[1]] % 4 != 2 and maze[s[0],s[1]] % 4 != 3 and [s[0]+1,s[1]] not in spaces_good:
                spaces_check.append([s[0]+1,s[1]])
                spaces_good.append([s[0]+1,s[1]])
        spaces_check.remove(s)

print(spaces_good)
print(time() - t)