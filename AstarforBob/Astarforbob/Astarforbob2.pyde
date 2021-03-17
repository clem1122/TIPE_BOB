
from bobclasses import *
from astarfonctions import *
from variables import *
from gridfunctions import *

objectif = Node(90, 13, 'a')

def setup():
    size(1400, 400, P2D)
    global objectif
    BuildObstruction(GRID, width // s, height // s)
    BuildObstacle2(GRID, width // s, height // s)

    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)

    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(700, 30, 700, 370)
    #voiture = Barrier(30, 30, 30, 370)

   # obstacle1 = Ground(300, 175, 300, 215)
   # obstacle2 = Ground(300, 175, 330, 145)
   # obstacle3 = Ground(300, 215, 330, 245)
    obstacle4 = Ground(510, 120, 525, 185)
    obstacle5 = Ground(525, 210, 510, 270)
    circle1 = Circle(320, 195, 30)
    grounds.append(up1)
    grounds.append(dn1)

    #grounds.append(obstacle1)
    #grounds.append(obstacle2)
    #grounds.append(obstacle3)
    grounds.append(obstacle4)
    grounds.append(obstacle5)

    grounds.append(depart)
    grounds.append(barrier)
    
    # grounds.append(voiture)
    
    circles.append(circle1)

    for i in range(nb_bobs):
        bobs.append(Bob(listPos[i][0], listPos[i][1], bob_radius, i,  objectif, grounds, circles, GRID))
        #bobs.append(Bob(random(10,280), random(160,270), bob_radius,i))
    for bob in bobs:
        bob.bobs = bobs
        

def draw():
    global j
    global barrier
    global GRID
    clear()
    noStroke()
    fill(0, 15)
    #wall1 = grounds[0]
    displayNode(objectif)
    displayObstruction()
    displayObstacle2()
    

    for bob in bobs:
        # if j%70==0:
        #    path = bob.Astar(objectif, GRID)
        if bob.position.x < width:
            bob.move(j)
            bob.display()
        else:
            bob.position.x = 5  # 2*width

    fill(127)
    for ground in grounds:
        stroke(ground.colour[0], ground.colour[1], ground.colour[2])
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
        grounds[-1].activate()
    for c in circles:
        c.display()
        #grounds[-1].follow(grounds[-2], 265)
    j += 1
    # saveFrame()
