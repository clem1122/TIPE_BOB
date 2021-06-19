from bobclasses import *
from variables import *
from gridfunctions import *
# SOMMAIRE
#
# objectif (built)
#
# SetBobFamily
# SetGrounds1
# SetGrounds2

objectif = Node(90, 13, 'a')

def SetBobFamily():
    for i in range(nb_bobs):
        bobs.append(Bob(random(30,235), random(125,265), bob_radius,i, objectif, grounds, circles, GRID))
    for bob in bobs:
        bob.bobs = bobs
    return 

def SetGrounds():
    global grounds
    global circles
    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)
    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(700, 30, 700, 370)
    obstacle4 = Ground(485, 120, 495, 165)
    obstacle5 = Ground(495, 225, 485, 270)
    circle1 = Circle(320, 195, 25)
    grounds.append(up1)
    grounds.append(dn1)
    grounds.append(obstacle4)
    grounds.append(obstacle5)
    grounds.append(depart)
    grounds.append(barrier)
    circles.append(circle1)
    return 

def SetCircle():
    global grounds
    global circles
    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)
    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(700, 30, 700, 370)
    circle1 = Circle(320, 195, 25)
    grounds.append(up1)
    grounds.append(dn1)
    grounds.append(depart)
    grounds.append(barrier)
    circles.append(circle1)
    return 
