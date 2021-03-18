from bobclasses import *
from astarfonctions import *
from variables import *
from gridfunctions import *
from setupfunctions import *

def setup():
    size(width, height, P2D)
    
    SetBobFamily()
    SetGrounds2()
    BuildObstacle2(GRID, w, h)
    BuildObstruction(GRID, w, h)

def draw():
    global j
    clear()
    
    displayNode(objectif)
    displayObstruction()
    displayObstacle2()
    
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
