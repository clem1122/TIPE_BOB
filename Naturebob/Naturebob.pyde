
from bobclasses import *
from variables import *


def setup():
    size(1400, 400, P2D)
    global objectif


    up1 = Ground(0, 120, 1400, 120)
    dn1 = Ground(0, 270, 1400, 270)

    depart = Ground(30, 370, 30, 30)
    barrier = Barrier(300, 30, 300, 370)

    grounds.append(up1)
    grounds.append(dn1)



    grounds.append(depart)
    grounds.append(barrier)
    
    # grounds.append(voiture)
    

    for i in range(nb_bobs):
        bobs.append(Bob(listPos[i][0], listPos[i][1], bob_radius, i,  grounds, circles))
        #bobs.append(Bob(random(10,280), random(160,270), bob_radius,i))
    for bob in bobs:
        bob.bobs = bobs
        

def draw():
    global j
    global barrier
    clear()
    noStroke()
    fill(0, 15)
    #wall1 = grounds[0]

    

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
