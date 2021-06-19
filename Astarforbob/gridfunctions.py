from bobclasses import *

# sommaire

# BuildGrid
# BuildObstruction
# displayObstruction
# displayObstacle
# BuildObstacle

# GRID (built)

def SetCircles():
    circles = []
    circle1 = Circle(320, 195, 25)
    circles.append(circle1)
    return circles
    
def BuildGrid(wi, he):
    w = wi // s
    h = he // s
    GRID = [[Node(i, j, 'o') for i in range(w)] for j in range(h)]
    return GRID

def BuildObstruction(GRID, w, h): 
    for i in range(130 // s, 185 // s):
        GRID[i][480 // s].nature = '!'
        GRID[i][515 // s].nature = '!'
    for i in range(125 // s, 195 // s):
        GRID[i + 7][480 // s].nature = '!'
        GRID[i + 7][515 // s].nature = '!'
    for i in range(w):
        GRID[120 // s][i].nature = '!'  
    for i in range(w):
        GRID[275 // s][i].nature = '!'

def displayObstruction():
    for i in range(130 // s, 185 // s):
        displayNode(GRID[i][480 // s])
        displayNode(GRID[i][515 // s])
    for i in range(125 // s, 180 // s):
        displayNode(GRID[i + 7][480 // s])
        displayNode(GRID[i + 7][515 // s])
    
def displayObstacle():
    for i in range((310 // s), (350 // s)):
        if i == (310 // s) or i == (350 // s)-1:
            for j in range(190//s , 235//s ):
                displayNode(GRID[j][i])  
        else:
            for j in range(175//s , 240//s ):
                displayNode(GRID[j][i])  
                displayNode(GRID[195//s][(345 // s)])
    
def BuildObstacle(GRID, w, h):
    for i in range((310 // s), (350 // s)):
        if i == (310 // s) or i == (350 // s)-1:
            for j in range(190//s , 235//s ):
                GRID[j][i].nature = '!'
        else:
            for j in range(175//s , 240//s ):
                GRID[j][i].nature = '!'
                GRID[195//s][(345 // s)].nature = '!'
    
GRID = BuildGrid(width, height)
