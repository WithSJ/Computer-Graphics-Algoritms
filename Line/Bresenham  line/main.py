from graphics import *
from time import sleep

win = GraphWin(title="Bresenham's algo",width=500,height=500)
def line(x1,y1,x2,y2):

    #calculate change in x and y
    dx = x2-x1
    dy = y2-y1

    if abs(dx)>abs(dy):
        p = 2*dy - dx
        while(x1<=x2):
            point = Point(x1,y1)
            print(x1,y1)
            point.draw(win)
            x1 += 1
            if(p<0):
                p = p + 2*dy
            else:
                p = p + 2*dy-2*dx
                y1 += 1
    else:
        p = 2*dx - dy
        while(y1<=y2):
            point = Point(x1,y1)
            print(x1,y1)
            point.draw(win)
            y1 += 1
            if(p<0):
                p = p + 2*dx
            else:
                p = p + 2*dx-2*dy
                x1 += 1



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
