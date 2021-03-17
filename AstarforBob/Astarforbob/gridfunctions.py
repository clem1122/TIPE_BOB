from bobclasses import *
def BuildGrid(wi, he):
    w = wi // s
    h = he // s
    GRID = [[Node(i, j, 'o') for i in range(w)] for j in range(h)]
    return GRID

def BuildObstruction(GRID, w, h): 
    for i in range(130 // s, 195 // s):
        GRID[i][510 // s].nature = '!'
        GRID[i][545 // s].nature = '!'
    for i in range(115 // s, 195 // s):
        GRID[i + 7][510 // s].nature = '!'
        GRID[i + 7][545 // s].nature = '!'
    for i in range(w):
        GRID[120 // s][i].nature = '!'  
    for i in range(w):
        GRID[275 // s][i].nature = '!'

def BuildObstacle1(GRID, w, h):
    
    for j in range((160 // s) + 2, (240 // s) - 1):
        GRID[j][300 // s].nature = '!'
    for i in range((160 // s) + 1, (240 // s) - 3):
        GRID[i + 4][(300 // s) + i - 10].nature = '!'
    for i in range((160 // s) + 1, (240 // s) - 3):
        GRID[i - 1][(300 // s) - i - 80].nature = '!'
    for j in range((160 // s) + 2, (240 // s) - 1):
        GRID[j][315 // s].nature = '!'
    for j in range((160 // s) + 1, (240 // s)):
        GRID[j][330 // s].nature = '!'



def displayObstruction():
    
    for i in range(130 // s, 195 // s):
        displayNode(GRID[i][510 // s])
        displayNode(GRID[i][545 // s])
    for i in range(115 // s, 180 // s):
        displayNode(GRID[i + 7][510 // s])
        displayNode(GRID[i + 7][545 // s])
    # for i in range(w):
    #     displayNode(GRID[120 // s][i])  
    #     displayNode(GRID[275 // s][i])  

def displayObstacle1():
    for i in range((160 // s) + 2, (240 // s) - 1):
        displayNode(GRID[i][300 // s])  
    for i in range((160 // s) + 1, (240 // s) - 3):
        displayNode(GRID[i + 4][(300 // s) + i - 10])  
    for i in range((160 // s) + 1, (240 // s) - 3):
        displayNode(GRID[i - 1][(300 // s) - i - 80])  
    for i in range((160 // s) + 2, (240 // s) - 1):
        displayNode(GRID[i][315 // s])  
    for i in range((160 // s) + 1, (240 // s)):
        displayNode(GRID[i][330 // s])  
    
def displayObstacle2():
    for i in range((310 // s), (360 // s)):
        if i == (310 // s) or i == (360 // s)-1:
            for j in range(190//s , 235//s ):
                displayNode(GRID[j][i])  
        else:
            for j in range(175//s , 240//s ):
                displayNode(GRID[j][i])  
    displayNode(GRID[195//s][(295 // s)])
    

def BuildObstacle2(GRID, w, h):
    for i in range((310 // s), (360 // s)):
        if i == (310 // s) or i == (360 // s)-1:
            for j in range(190//s , 235//s ):
                GRID[j][i].nature = '!'
        else:
            for j in range(175//s , 240//s ):
                GRID[j][i].nature = '!'
    GRID[195//s][(295 // s)].nature = '!'
    





GRID = BuildGrid(width, height)
