from variables import *
def displayNode(node):
    noStroke()
    if node.nature == 's':
        fill(30, 230, 180)
        circle(s * node.x, s * node.y, 5)
    elif node.nature == 'a':
        fill(255, 255, 76)
        circle(s * node.x, s * node.y, 5)
    elif node.nature == 'o':
        fill(150, 200, 255)
        circle(s * node.x, s * node.y, 5)
    elif node.nature == 'p':
        noStroke()
        fill(100, 230, 170)
        circle(s * node.x, s * node.y, 5)
    elif node.nature == '!':
        noStroke()
        fill(120, 20, 40)
        circle(s * node.x, s * node.y, 5)

def reconstituer_chemin(node, start):
    path = []
    N = node
    while not(N.x == start.x and N.y == start.y):
        path.append(N)
        N = N.parent
    return path

def manhattan(n1, n2):
    distance = (abs(n1.x - n2.x) + abs(n1.y - n2.y))
    return 10 * distance

def euclide(n1, n2):
    distance = sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)
    return 10 * distance

def clef(node):
    return (node.F, node.H)
