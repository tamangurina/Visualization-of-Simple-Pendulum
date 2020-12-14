from graphics import *
import math
import time
 
#VARIABLES
width, height = 800, 400   # set the width and height of the window
Out = False                # if True,out of while loop
acceleration = False       # when true it allow us to find the acceleration and damping for the pendulum
velocity = 0               # velocity that angle is increased and damped
Aacceleration = 0          # acceleration

angle = int(input("Enter the angular displacement: "))  # the angle that you begin in window
length = int(input("Enter the length of string: "))     # the length between the ball and the support


class ball(object):
 
    def __init__(self, XY, radius):  # Set ball coordenates and radius
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius
 
    def draw(self, win):  # Draw circle and line based on XY coordinates
        pivot = Rectangle(Point(width/2 -50 , 50), Point(width/2 + 50, 55))
        pivot.setFill("grey")
        pivot.draw(win) 

        string = Line(Point(width/2, 50), Point(self.x, self.y))
        string.setOutline("black")
        string.draw(win)

        bob_ = Circle(Point(self.x, self.y), self.radius)
        bob_.setOutline("black")
        bob_.draw(win)
        bob = Circle(Point(self.x, self.y), self.radius - 1)
        bob.setFill("blue") 
        bob.draw(win)
  
def get_path(first_angle, length): # with angle and length calculate x and y position
    pendulum.x = round(width/2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))
 
def redraw(win):  # update window with a new frame of pendulum 
    pendulum.draw(win)
    update()

def clear(win):     # clean up the screen
    for item in win.items[:]:
        item.undraw()


pendulum = ball((int(width / 2), length), 15)

def main():

    global velocity, Aacceleration, angle, length
    
    win = GraphWin('SHM - Pendulum', width, height, autoflush = False)
    win.setCoords(799, 399, 0, 0)
    
    while not Out:
        clear(win)
        time.sleep(.08)        
        acceleration = True                     
    
        if acceleration:   # Increase acceleration and damping in the pendulum movement
            Aacceleration = -0.005 * math.sin(angle)
            velocity += Aacceleration
            velocity *= 0.99  # damping factor
            angle += velocity
            get_path(angle, length)        
 
        redraw(win)
    
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()

