from bobclasses import *
from variables import *
from gridfunctions import *
# SOMMAIRE
#
# objectif (built)
#
#
# SetBobFamily
# SetGrounds1
# SetGrounds2


objectif = Node(90, 13, 'a')

def SetBobFamily():
    
    for i in range(nb_bobs):
        bobs.append(Bob(listPos[i][0], listPos[i][1], bob_radius, i,  objectif, grounds, circles, GRID))
        #bobs.append(Bob(random(10,280), random(160,270), bob_radius,i))
    for bob in bobs:
        bob.bobs = bobs
    
    return 

def SetGrounds1():
    global grounds
    global circles
    
    
    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)

    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(700, 30, 700, 370)
    
    obstacle1 = Ground(300, 175, 300, 215)
    obstacle2 = Ground(300, 175, 330, 145)
    obstacle3 = Ground(300, 215, 330, 245)
    obstacle4 = Ground(510, 120, 525, 185)
    obstacle5 = Ground(525, 210, 510, 270)
    
    grounds.append(up1)
    grounds.append(dn1)
    
    grounds.append(obstacle1)
    grounds.append(obstacle2)
    grounds.append(obstacle3)
    grounds.append(obstacle4)
    grounds.append(obstacle5)

    grounds.append(depart)
    grounds.append(barrier)
    
    return 

def SetGrounds2():
    global grounds
    global circles
    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)

    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(700, 30, 700, 370)
    
    obstacle4 = Ground(510, 120, 525, 185)
    obstacle5 = Ground(525, 210, 510, 270)
    circle1 = Circle(320, 195, 30)
    
    grounds.append(up1)
    grounds.append(dn1)
    
    grounds.append(obstacle4)
    grounds.append(obstacle5)
    grounds.append(depart)
    grounds.append(barrier)
    circles.append(circle1)
    
    return 
