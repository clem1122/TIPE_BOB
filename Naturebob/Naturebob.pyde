from bobclasses import *
from variables import *
from setupfunctions import *

def setup():
    size(width, height, P2D)
    
    SetBobFamily()
    SetGrounds1()

def draw():
    global j
    clear()
    
    for bob in bobs:
        bob.move(j)
        bob.display()

    for ground in grounds:
        ground.display()
        grounds[-1].activate()
        
    for c in circles:
        c.display()
        
    j += 1
    # saveFrame()
