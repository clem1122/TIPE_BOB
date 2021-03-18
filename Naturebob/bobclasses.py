from variables import *

# SOMMAIRE
#
#
# Bob
#    - init
#    - move
#    - display
#    - g
#    - CheckOtherCollision
#    - CircleCollision
#    - WallCollision
#    - FrictionForce
#    - FollowMouse
#    - NeedForSpeed
#    - intersection
#    - Astar
#    - setDirection


# Ground
#    - init
#    - update
#    - display
# --> Barrier
#    - activate
#    - follow

# Circle
#    - init
#    - display


class Bob:
    
    def __init__(self, x, y, radius, index, grounds, circles):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.index = index
        self.obj = PVector(1200 - 3 * radius, 200)
        self.masse = random(75, 100)
        self.radius = radius * self.masse / maxmasse
        self.e = PVector(1, 0)
        self.grounds = grounds
        self.circles = circles
        self.bobs = []
        
        

        self.A = 30
        self.B = 5
        self.k = 10
        self.K = 0
        self.kw = 30

    def move(self, j):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.acceleration.add(self.CheckOtherCollision())
        self.acceleration.add(self.NeedForSpeed(self.e, self.grounds[-1]))
        self.acceleration.add(self.CircleCollision(self.circles))
        self.acceleration.add(self.WallCollision(self.grounds))
        self.acceleration.mult(1 / self.masse)

    def display(self):

        fill(200)
        noStroke()
        circle(self.position.x, self.position.y, self.radius * 2)

    def g(self, x):
        return (x >= 0) * x + 0

    def CheckOtherCollision(self):

        F = PVector(0, 0)
        for other in self.bobs:
            if other.index != self.index:
                dij = (self.position - other.position).mag()
                nij = (self.position - other.position).normalize()
                rij = self.radius + other.radius
                tij = nij.copy()
                tij.rotate(HALF_PI)
                stroke(255, 0, 0)
                DeltaVij = (other.velocity - self.velocity).dot(tij)
                fij = (self.A * exp((rij - dij) / self.B) + self.k * self.g(rij - dij)
                       ) * nij + (self.K * self.g(rij - dij) * DeltaVij) * tij
                F.add(fij)
        return F
    
    def CircleCollision(self, circles):
        F = PVector(0, 0)
        for c in circles:

            d = (self.position - c.center).mag()
            n = (self.position - c.center).normalize()
            r = self.radius + c.radius
            t = n.copy()
            t.rotate(HALF_PI)
            stroke(255, 0, 0)

            
            fic = (self.A * exp((1.2 * r - d) / self.B) + self.kw * self.g(1.2 * r - d)
                       ) * n + (self.K * self.g(r - d) * (self.velocity.dot(t))) * t
            F.add(fic)
        return F

    def WallCollision(self, grounds):
        F = PVector(0, 0)

        for ground in grounds:

       
            v = ground.b - ground.a
            v.normalize()

            I = PVector(self.position.x - ground.x, self.position.y - ground.y)
            P = v.mult(v.dot(I))
            H = PVector(P.x + ground.x, P.y + ground.y)

            
            def isInSegment(H, ground):
                vA = ground.a - H
                vB = ground.b - H
                return vA.dot(vB) <= 0

            if isInSegment(H, ground):
                r = self.radius
                diw = (self.position - H).mag()
                n = (self.position - H).normalize()
                stroke(255, 0, 0)
                t = n.copy().rotate(HALF_PI)

                fiw = (self.A * exp((1.2 * r - diw) / self.B) + self.kw * self.g(1.2 * r - diw)
                       ) * n + (self.K * self.g(r - diw) * (self.velocity.dot(t))) * t
                F.add(fiw)
        return F

    def FrictionForce(self):
        f = self.velocity.copy()
        norme = f.mag()
        f.normalize()
        f *= -friction
        f.setMag(norme * norme)
        return f

    def FollowMouse(self):
        if mousePressed:
            ax = -(mouseX - self.position.x)
            ay = -(mouseY - self.position.y)
            return PVector(0, 0)
        else:
            ax = mouseX - self.position.x
            ay = mouseY - self.position.y
            return PVector(ax, ay).setMag(MouseMag)


    def NeedForSpeed(self, e, barrier):


        F = PVector(0, 0)
        if barrier.state == 'g':
            F = (vi * e - self.velocity) / tau
        elif barrier.state == 'b':
            F = (-vi * e - self.velocity) / tau
        else:
            F = (vi * e - self.velocity) / tau
        return F

    def intersection(self, ground):
        L = ground.a
        E = ground.b
        C = self.position
        d = E.copy().sub(L)
        r = self.radius
        f = C.copy().sub(E)
        a = d.dot(d)
        b = 2 * f.dot(d)
        c = f.dot(f) - r * r
        delta = b * b - 4 * a * c
        t1 = (-b - sqrt(delta)) / (2 * a)
        t2 = (-b + sqrt(delta)) / (2 * a)
        T1 = E.copy().add(d.copy().mult(-t1))
        T2 = E.copy().add(d.copy().mult(-t2))

        return (delta > 0 and t1 >= 0 and t1 <= 1 or (t2 >= 0 and t2 <= 1))



class Ground:

    def __init__(self, x1, y1, x2, y2):
        self.a = PVector(x1, y1)
        self.b = PVector(x2, y2)
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        self.colour = (255, 255, 255)
        
    def display(self):
        stroke(self.colour[0], self.colour[1], self.colour[2])
        line(self.a.x, self.a.y, self.b.x, self.b.y)

    def update(self):
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))


class Barrier(Ground):

    def __init__(self, x1, y1, x2, y2):
        Ground.__init__(self, x1, y1, x2, y2)
        self.state = 'r'
        self.colour = (255, 0, 0)

    def activate(self):
        if keyPressed:
            self.state = 'g'
            self.colour = (0, 255, 0)
            self.a.x += v_barrier
            self.b.x += v_barrier
            self.x = (self.a.x + self.b.x) / 2
            self.y = (self.a.y + self.b.y) / 2
            self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
            self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        elif mousePressed:
            self.state = 'b'
            self.colour = (0, 0, 255)
            self.a.x -= v_barrier
            self.b.x -= v_barrier
            self.x = (self.a.x + self.b.x) / 2
            self.y = (self.a.y + self.b.y) / 2
            self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
            self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        else:
            self.state = 'r'
            self.colour = (255, 0, 0)
            self.x = (self.a.x + self.b.x) / 2
            self.y = (self.a.y + self.b.y) / 2
            self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
            self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))

    def follow(self, barrier, seuil):
        if barrier.state == 'r':
            if abs(self.x - barrier.x) > seuil:
                self.state = 'g'
                self.colour = (0, 255, 0)
                self.a.x += v_barrier / 10
                self.b.x += v_barrier / 10
                self.x = (self.a.x + self.b.x) / 2
                self.y = (self.a.y + self.b.y) / 2
                self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
                self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
class Circle:
    
    def __init__(self, x, y, r):
        self.center = PVector(x,y)
        self.radius = r
    
    def display(self):
        stroke(255)
        noFill()
        circle(self.center.x, self.center.y, 2*self.radius)
