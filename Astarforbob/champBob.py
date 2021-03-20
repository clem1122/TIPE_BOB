import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patch

n = 32 # nb_bobs

# murs et obstacles

wx1 = [0,1400]
wy1 = [120,120]

wx2 = [0,1400]
wy2 = [270,270]

wx3 = [510, 525]
wy3 = [120, 185]

wx4 = [525, 510]
wy4 = [210, 270]

plt.plot(wx1,wy1, color = 'black')
plt.plot(wx2,wy2, color = 'black')
plt.plot(wx3,wy3, color = 'black')
plt.plot(wx4,wy4, color = 'black')

cercle = patch.Ellipse((320, 195), 60, 60, angle=0)
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.add_artist(cercle)
cercle.set_facecolor('black')

# trajectoires des bobs

for i in range(n):

    X = open("/Users/ninasato/Desktop/Astarforbob/X/positionX"+str(i)+".txt", mode = "r")
    Y = open("/Users/ninasato/Desktop/Astarforbob/Y/positionY"+str(i)+".txt", mode = "r")

    for line in X:
        a = line
    for line in Y:
        b = line

    bx_ = a.split(', ')
    by_ = b.split(', ')

    bx = bx_[:400]
    by = by_[:400]
    bobX = [float(x) for x in bx]
    bobY = [float(y) for y in by]

    plt.plot(bobX,bobY,color = "red", lw = '0.5')

# calibrage des axes

plt.axis([0, 1400, 0, 400])
plt.show()

