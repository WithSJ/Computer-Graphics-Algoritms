from graphics import *
from time import sleep

win = GraphWin(title="DDA algo",width=500,height=500)

def line(x1,y1,x2,y2):

    #calculate change in x and y
    dx = x2-x1
    dy = y2-y1
    
    #steps is equal to greater change
    steps = abs(dx) if abs(dx)>abs(dy) else abs(dy)

    # how much should incress values in x and y
    xinc = dx/steps
    yinc = dy/steps

    for _ in range(steps):
        
        x1 = x1+xinc
        y1 = y1+yinc

        point = Point(int(x1),int(y1))
        print(int(x1),int(y1))
        point.draw(win)

def run():
    print("Click on screen for input start point of line")
    start_point = win.getMouse()
    print("Click on screen for input end point of line")
    end_point = win.getMouse()

    line(int(start_point.x),int(start_point.y),int(end_point.x),int(end_point.y))

while True:
    run()

print("Click on screen for exit")
win.getMouse()
win.close()
