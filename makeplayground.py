from tkinter import *
from tkinter import ttk
from runmaze import runmaze
from time import time

x=100
y=100
x_s = 10
y_s = 10

maze = runmaze(x,y)

# p = position within the maze, l = location on the local map
p = (0,0)
l = [5,5]

# m will be the map horizontal and vertical segments
m_h = [None]*(x_s*y_s)
m_v = [None]*(x_s*y_s)

def move(p):
    print('hello')

def frame(l):
    ttk.Label(mf,text="").grid(column=l[0]*2+1,row=l[1]*2+1)
    if l == [5,5]: l = [6,6]
    elif l == [6,6]: l = [5,5]
    ttk.Label(mf,text="x").grid(column=l[0]*2+1,row=l[1]*2+1)

def build(top,left):
    print('stuff')

# begin the game loop
root = Tk()
root.title("   M a z e   ")

mf = ttk.Frame(root,padding=(5,5,5,5)).grid(row=0,column=0)

# Need to fix the indicies on this!!!!!!!
for i in range(x_s):
    for j in range(y_s):
        m_v[i + j*x_s] = ttk.Frame(mf,height=20,width=4,borderwidth=2,relief='sunken').grid(column=2*i,row=2*j+1)
        m_h[i + j*x_s] = ttk.Frame(mf,height=4,width=20,borderwidth=2,relief='sunken').grid(column=2*i+1,row=2*j)
for i in range(x_s):
    ttk.Frame(mf,height=4,width=20,borderwidth=2,relief='sunken').grid(column=2*i+1,row=2*y_s)
for j in range(y_s):
    ttk.Frame(mf,height=20,width=4,borderwidth=2,relief='sunken').grid(column=2*x_s,row=2*j+1)

root.update()
while True:
    try:
        t = time()
        build(0,0)
        root.after(10,frame(l))
        if l == [5,5]:
            l = [6,6]
        elif l == [6,6]:
            l = [5,5]
        root.update()
        print(time()-t)
    except:
        exit()
        pass
root.mainloop()
