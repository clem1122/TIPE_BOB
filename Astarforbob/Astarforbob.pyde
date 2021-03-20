from bobclasses import *
from astarfonctions import *
from variables import *
from gridfunctions import *
from setupfunctions import *

def setup():
    global Y
    global X
    size(width, height, P2D)
    
    SetBobFamily()
    SetGrounds2()
    BuildObstacle2(GRID, w, h)
    BuildObstruction(GRID, w, h)
    
    X = []
    Y = []
    for i in range(nb_bobs):
        X.append(createWriter("X/positionX"+str(i)+".txt"))
        Y.append(createWriter("Y/positionY"+str(i)+".txt"))

def draw():
    global j

    
    clear()
    
    displayNode(objectif)
    displayObstruction()
    displayObstacle2()
    
    for bob in bobs:
        bob.move(j)
        bob.display()
        
        X[bob.index].print(bob.position.x)
        X[bob.index].print(", ")
        Y[bob.index].print(bob.position.y)
        Y[bob.index].print(", ")

    for ground in grounds:
        ground.display()
        grounds[-1].activate()
        
    for c in circles:
        c.display()
        
    j += 1
    # saveFrame()
