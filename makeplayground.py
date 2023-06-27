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
m_h = [None]*((x_s)*(y_s+1))
m_v = [None]*((x_s+1)*(y_s))

def move(p):
    pass

def frame(l):
    ttk.Label(mf,text="").grid(column=l[0]*2+1,row=l[1]*2+1)
    if l == [5,5]: l = [6,6]
    elif l == [6,6]: l = [5,5]
    ttk.Label(mf,text="x").grid(column=l[0]*2+1,row=l[1]*2+1)

def build(tl):
    t = int(tl[0])
    l = int(tl[1])
    for i in range(x_s+1):
        for j in range(y_s):
            if (i,j) == (0,0): continue

            # If the top and left rows end off the maze definions
            # then assign the current space a blank
            try: s = maze[(str(l+i-1),str(t+j-1))]
            except: s = blank

            if s[0] == 1:
                m_v[i+j*y_s]['relief']='sunken'
            else:
                m_v[i+j*y_s]['relief']='flat'
            if s[1] == 1:
                print(i+j*y_s)
            else:
                print(i+j*y_s)

#def build(j):
#    print(len(m_v),len(m_h))
#    for i in range(len(m_v)):
#        m_v[i]['relief']='flat'
#    for i in range(len(m_h)):
#        m_h[i]['relief']='flat'
#
# begin the game loop
root = Tk()
root.title("   M a z e   ")

mf = ttk.Frame(root,padding=(5,5,5,5)).grid(row=0,column=0)

# initiate the maze and map each wall to a different index in m_v and m_h
# converting k to vertical: [x,y]=[k%(x_s+1),(k-j_v)/(x_s+1)]
i_v, j_v, i_h, j_h = 0, 0, 0, 0
for k in range((x_s+1)*(y_s+1)):
    if j_v < y_s: 
        m_v[k] = ttk.Frame(mf,height=20,width=4,borderwidth=2,relief='sunken')
        m_v[k].grid(column=2*i_v,row=1+2*j_v)
        print(k)
    if i_h < x_s: 
        m_h[k] = ttk.Frame(mf,height=4,width=20,borderwidth=2,relief='sunken')
        m_h[k].grid(column=1+2*i_h,row=2*j_h)
    i_v, j_h = (i_v+1)%(x_s+1), (j_h+1)%(y_s+1)
    if i_v == 0: j_v += 1
    if j_h == 0: i_h += 1

root.update()
while True:
    try:
        t = time()
        build(('0','0'))
        root.after(100,frame(l))
        if l == [5,5]:
            l = [6,6]
        elif l == [6,6]:
            l = [5,5]
        root.update()
        print(time()-t)
    except:
        print('found an error')
        exit()
        pass
root.mainloop()
