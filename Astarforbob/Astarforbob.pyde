from bobclasses import *
from astarfonctions import *
from variables import *
from gridfunctions import *
from setupfunctions import *

def setup():
    global Y
    global X
    global Vx
    global Vy
    size(width, height, P2D)
    
    SetBobFamily()
    SetGrounds()
    BuildObstacle(GRID, w, h)
    BuildObstruction(GRID, w, h)
    X = []
    Y = []
    Vx = []
    Vy = [] 
    for i in range(nb_bobs):
        X.append(createWriter("X/positionX"+str(i)+".txt"))
        Y.append(createWriter("Y/positionY"+str(i)+".txt"))
        Vx.append(createWriter("Vx/vitesseX"+str(i)+".txt"))
        Vy.append(createWriter("Vy/vitesseY"+str(i)+".txt"))

def draw():
    global j

    clear()
    
    displayNode(objectif)
    displayObstruction()
    displayObstacle()
    
    for bob in bobs:
        bob.move(j)
        bob.display()
        
        X[bob.index].print(bob.position.x)
        X[bob.index].print(", ")
        Y[bob.index].print(bob.position.y)
        Y[bob.index].print(", ")
        Vx[bob.index].print(bob.velocity.x)
        Vx[bob.index].print(", ")
        Vy[bob.index].print(bob.velocity.y)
        Vy[bob.index].print(", ")
         

    for ground in grounds:
        
        ground.display()
        grounds[-1].activate()
        
    for c in circles:
        c.display()
        
    j += 1
    if j>10:
        saveFrame()
