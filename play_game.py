from tkinter import *
from tkinter import ttk
from runmaze import runmaze
from time import *
from math import *
import keyboard

# x and y are dimensions of the overall maze, x_s and y_s are 
# dimensions of the local map
x=30
y=30
x_s = 11
y_s = 11
x_2 = floor(x_s/2)
y_2 = floor(y_s/2)

# Build out the x by y maze and define a blank space for any
# functions which need to use a space outside the bounds of the maze
maze, goal = runmaze(x,y)
blank = [0,0,'empty']

# p = position within the maze, ps = location on the local map
p = [0,0]
p_s = [0,0]

# initiate a key pressed variable
kp = 'zzz'

# w will be the horizontal and vertical walls for the local map
w_h = [[None for i in range(y_s+1)] for j in range(x_s)]
w_v = [[None for i in range(y_s)] for j in range(x_s+1)]

#Initialize refresh timer for keystrokes
refresh = [0.03, 0.1]
t = dict()
for a in 'qweasd': t[a] = t.get(a,0)
t['up'] = t.get('up',0)

def checkmove(a):
    if a == 'zzz': return False
    if a == 'a': dp, i = (p[0]-1,p[1]), 0
    if a == 's': dp, i = (p[0],p[1]), 1
    if a == 'd': dp, i = (p[0],p[1]), 0
    if a == 'w': dp, i = (p[0],p[1]-1), 1
    try: 
        if maze[dp][i] == 1: return False
    except: pass
    return True

def build(p):
    i_0 = min(max(p[0]-x_2,0),x-x_s)-1
    j_0 = min(max(p[1]-y_2,0),y-y_s)-1

    try: p_g.destroy()
    except: pass

    for i in range(x_s+1):
        for j in range(y_s+1):
            # If the top and left rows end off the maze definions
            # then assign the current space a blank
            if i_0+i >= 0 and i_0+i <= x-2 and j_0+j>=0 and j_0+j <= y-2:
                s = maze[(i_0+i,j_0+j)]
            else: 
                s = blank

#            if (i_0+i,j_0+j) == goal:
#                p_g = Frame(mf,height=20,width=20,background='blue')
#                p_g.grid(column=(i_0+i)*2+1,row=(j_0+j)*2+1)

            if s[0]==0: w_v[i][j-1]['relief']='flat'
            elif s[0]==1: w_v[i][j-1]['relief']='sunken'

            if s[1]==0: w_h[i-1][j]['relief']='flat'
            elif s[1]==1: w_h[i-1][j]['relief']='sunken'

    # check to see if the position on the local map moved
    p_t = [min(p[0],max(p[0]+x_s-x,x_2)),
           min(p[1],max(p[1]+y_s-y,y_2))]
    # if the position on the map has moved, update the x
    p_x.grid(column=p_t[0]*2+1,row=p_t[1]*2+1)

def frame_update(p):
    try:
        #t = time()
        build(p)
        root.update()
        #print(time()-t)
    except Exception as exc:
        print('found an error')
        print(exc)
        exit()

# -----------------------------------------------------------------------
# begin building the GUI
root = Tk()
root.title("   M a z e   ")

# build a frame to put all the walls into
mf = ttk.Frame(root,padding=5)
mf.grid(row=0,column=0)

# define a blank position and a character position. Every time
# the char moves, p_x will be placed and the old position will
# be replaced with p_b
p_x = Frame(mf,height=20,width=20,background='green')
p_x.grid(column=p_s[0]*2+1,row=p_s[1]*2+1)

# map each wall to vertical m_v and horizontal m_h walls
for i in range(x_s+1):
    for j in range(y_s+1):
        if j < y_s:
            w_v[i][j] = ttk.Frame(mf,height=20,width=4,borderwidth=2,relief='sunken')
            w_v[i][j].grid(column=2*i,row=1+2*j)
        if i < x_s:
            w_h[i][j] = ttk.Frame(mf,height=4,width=20,borderwidth=2,relief='sunken')
            w_h[i][j].grid(column=1+2*i,row=2*j)

frame_update(p)
while True:
    if keyboard.is_pressed('a'): kp, p_i, dp, b = 'a', 0, -1, 0
    if keyboard.is_pressed('s'): kp, p_i, dp, b = 's', 1, 1, y-1
    if keyboard.is_pressed('d'): kp, p_i, dp, b = 'd', 0, 1, x-1
    if keyboard.is_pressed('w'): kp, p_i, dp, b = 'w', 1, -1, 0
    
    if checkmove(kp): 
        if time()-t[kp]>refresh[1] and p[p_i]*dp<b:
            t[kp] = time()
            p[p_i] += dp
            print(p)

    if time() - t['up'] > refresh[0]:
        frame_update(p)
        t['up'] = time()
    kp = 'zzz'
    sleep(refresh[0])

root.mainloop()