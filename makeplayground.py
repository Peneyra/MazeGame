from tkinter import *
from tkinter import ttk
from runmaze import runmaze
from time import time

x=100
y=100
x_s = 11
y_s = 11

maze = runmaze(x,y)
blank = [0,0,'']

# p = position within the maze, l = location on the local map, tl = top left
p = ('0','0')
l = [5,5]
tl = ('0','0')

# m will be the map horizontal and vertical segments
m_h = [[None for i in range(y_s+1)] for j in range(x_s)]
m_v = [[None for i in range(y_s)] for j in range(x_s+1)]

def move(p):
    pass

def frame(l):
    ttk.Label(mf,text="").grid(column=l[0]*2+1,row=l[1]*2+1)
    if l == [5,5]: l = [6,6]
    elif l == [6,6]: l = [5,5]
    ttk.Label(mf,text="x").grid(column=l[0]*2+1,row=l[1]*2+1)

def build(tl):
    t = int(tl[0])-1
    l = int(tl[1])-1
    for i in range(x_s+1):
        for j in range(y_s+1):

            # If the top and left rows end off the maze definions
            # then assign the current space a blank
            try: s = maze[(str(l+i),str(t+j))]
            except: s = blank

            if j < y_s:
                if s[0]==0 and m_v[i][j]['relief']!='flat':
                    m_v[i][j]['relief']='flat'
                elif s[0]==1 and m_v[i][j]['relief']!='sunken':
                    m_v[i][j]['relief']='sunken'
            if i < x_s:
                if s[1]==0 and m_h[i][j]['relief']!='flat':
                    m_h[i][j]['relief']='flat'
                elif s[1]==1 and m_h[i][j]['relief']!='sunken':
                    m_h[i][j]['relief']='sunken'

# -----------------------------------------------------------------------
# begin building the GUI
root = Tk()
root.title("   M a z e   ")

# build a frame to put all the walls into
mf = ttk.Frame(root,padding=5)
mf.grid(row=0,column=0)

# map each wall to vertical m_v and horizontal m_h walls
for i in range(x_s+1):
    for j in range(y_s+1):
        if j < y_s:
            m_v[i][j] = ttk.Frame(mf,height=20,width=4,borderwidth=2,relief='sunken')
            m_v[i][j].grid(column=2*i,row=1+2*j)
        if i < x_s:
            m_h[i][j] = ttk.Frame(mf,height=4,width=20,borderwidth=2,relief='sunken')
            m_h[i][j].grid(column=1+2*i,row=2*j)

while True:
    try:
        t = time()
        build(tl)
        root.after(100,frame(l))
        root.update()
        print(time()-t)
    except:
        print('found an error')
        exit()
        pass
root.mainloop()
