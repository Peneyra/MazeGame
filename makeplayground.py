from tkinter import *
from tkinter import ttk
from runmaze import runmaze
from time import *
from math import *
import keyboard

# x and y are dimensions of the overall maze, x_s and y_s are 
# dimensions of the local map
x=100
y=100
x_s = 11
y_s = 11
x_2 = floor(x_s/2)
y_2 = floor(y_s/2)

# Build out the x by y maze and define a blank space for any
# functions which need to use a space outside the bounds of the maze
maze = runmaze(x,y)
blank = [0,0,'empty']

# p = position within the maze, ps = location on the local map
p = [0,0]
p_s = [0,0]

# w will be the horizontal and vertical walls for the local map
w_h = [[None for i in range(y_s+1)] for j in range(x_s)]
w_v = [[None for i in range(y_s)] for j in range(x_s+1)]

#Initialize refresh timer for keystrokes
refresh_key = 0.1
refresh = 0.03
t_a=0
t_s=0
t_d=0
t_w=0
t_q=0
t_e=0
t_update=0

def checkmove(a):
    if a == 'a':
        try: 
            if maze[(str(p[0]-1),str(p[1]))][0] == 1:
                return False
        except: pass
    if a == 's':
        try: 
            if maze[(str(p[0]),str(p[1]))][1] == 1:
                return False
        except: pass
    if a == 'd':
        try: 
            if maze[(str(p[0]),str(p[1]))][0] == 1:
                return False
        except: pass
    if a == 'w':
        try: 
            if maze[(str(p[0]),str(p[1]-1))][1] == 1:
                return False
        except: pass

    return True

def build(p,p_s):
    print('========================')
    print('start build')
    i_0 = min(max(p[0]-x_2,0),x-x_s)-1
    j_0 = min(max(p[1]-y_2,0),y-y_s)-1
    for i in range(x_s+1):
        for j in range(y_s+1):
            # If the top and left rows end off the maze definions
            # then assign the current space a blank
            #print(str(i_0+i),str(j_0+j))
            if i_0+i >= 0 and i_0+i <= x-2 and j_0+j>=0 and j_0+j <= y-2:
                s = maze[(str(i_0+i),str(j_0+j))]
            else: 
                s = blank
        #if j < y_s:
            if s[0]==0: w_v[i][j-1]['relief']='flat'
            elif s[0]==1: w_v[i][j-1]['relief']='sunken'
        #if i < x_s:
            if s[1]==0: w_h[i-1][j]['relief']='flat'
            elif s[1]==1: w_h[i-1][j]['relief']='sunken'

    # check to see if the position on the local map moved
    p_t = [min(p[0],max(p[0]+x_s-x,x_2)),
           min(p[1],max(p[1]+y_s-y,y_2))]
    # if the position on the map has moved, update the x
    p_b.grid(column=p_s[0]*2+1,row=p_s[1]*2+1)
    p_x.grid(column=p_t[0]*2+1,row=p_t[1]*2+1)
    return p_t

def frame_update(p,p_s):
    try:
        #t = time()
        p_s = build(p,p_s)
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
p_x = ttk.Label(mf,text="x")
p_b = ttk.Label(mf,text="")
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
#        if j< y_s and i < x_s:
#            ttk.Label(mf,text=str(i)+str(j)).grid(column=1+2*i,row=1+2*j)

frame_update(p,p_s)
while True:
    if keyboard.is_pressed('a'):
        if time() - t_a > refresh_key and checkmove('a'):
            if int(p[0]) > 0:
                t_a = time()
                p[0] = p[0]-1
                print(p)
    if keyboard.is_pressed('s'):
        if time() - t_s > refresh_key and checkmove('s'):
            if int(p[1]) < y-1:
                t_s = time()
                p[1] = p[1]+1
                print(p)
    if keyboard.is_pressed('d'):
        if time() - t_d > refresh_key and checkmove('d'):
            if int(p[0]) < x-1:
                t_d = time()
                p[0] = p[0]+1
                print(p)
    if keyboard.is_pressed('w'):
        if time() - t_w > refresh_key and checkmove('w'):
            if int(p[1]) > 0:
                t_w = time()
                p[1] = p[1]-1
                print(p)
    if time() - t_update > refresh and t_d != 0:
        frame_update(p,p_s)
        t_update = time()
    
    sleep(refresh)

root.mainloop()
