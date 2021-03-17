bobs = []
grounds = []
nb_bobs = 20
MouseMag = 0.1
RepMag = 250
WallMag = 100
ObjMag = 20
frot = 0.97
bob_radius = 10
maxmasse = 95
R = 100
grounds = []
friction = 0
bob_damp = 0.8
tau = 0.5
vi = 1
v_barrier = 1
nx = 100//(bob_radius+2)
ny = 320//(bob_radius+2)


x0 = (bob_radius+2)
y0 = (bob_radius+2)

savedlen = 500

j = 0




def setup():
    size(1400, 400, P2D)
    global grounds
    
    up1 = Ground(0,30,100,30)
    up2 = Ground(100,30,520,150)
    up3 = Ground(520, 150,620,150)
    up4 = Ground(620,150,1010,30)
    up5 = Ground(1010,30,1110,30)
    
    dn5 = Ground(1110,370,1010,370)
    dn4 = Ground(1010,370,620,280)
    dn3 = Ground(620,280,520,280)
    dn2 = Ground(520,280,100,370)
    dn1 = Ground(100,370,0,370)
    
    #obs1 = Ground(850,0,850,180)
    #obs2 = Ground(850,220,850,400)
    
    depart = Ground(0,370,0,30)
    
    objectif = Ground(1200,30,1200,370)
    barrier = Barrier(300, 30, 300,370)
    
    grounds.append(up1)
    grounds.append(up2)
    grounds.append(up3)
    grounds.append(up4)
    grounds.append(up5)
    
    grounds.append(dn1)
    grounds.append(dn2)
    grounds.append(dn3)
    grounds.append(dn4)
    grounds.append(dn5)
    
    #grounds.append(obs1)
    #grounds.append(obs2)
    
    grounds.append(depart)
    grounds.append(barrier)
    #grounds.append(objectif)
    
    for i in range(nb_bobs):
        bobs.append(Bob(random(10,380), random(110,310), bob_radius,i))
    
    
def draw():
    global objectif
    global j
    global barrier
    objectif = Ground(1200,370,1200,30)
    

    clear()
    noStroke()
    fill(0, 15)
    #wall1 = grounds[0]

    for bob in bobs:
        bob.acceleration.add(bob.WallCollision(grounds)/bob.masse)
        if bob.position.x<objectif.x:
            bob.move()
            bob.display()
        else:
            bob.position.x = 5 #2*width
    
    fill(127)
    for ground in grounds:
        stroke(ground.colour[0],ground.colour[1],ground.colour[2])
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
        grounds[-1].activate()
    stroke(255)
    line(objectif.a.x, objectif.a.y, objectif.b.x, objectif.b.y)

    
    
class Bob(object):

    def __init__(self, x, y, radius, index):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        self.index = index
        self.obj = PVector(1200-3*radius,200)
        self.masse = random(60,95)
        self.radius = radius* self.masse/maxmasse
        
        self.A = 2
        self.B = 3
        self.k = 10
        self.K = 0
        
        
    def move(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.acceleration.add(self.CheckOtherCollision())
        self.acceleration.add(self.NeedForSpeed(grounds[-1]))
        #self.acceleration.add(self.WallCollision(grounds[:len(grounds)-1]))
        self.acceleration.add(self.FrictionForce())
        self.acceleration.mult(1/self.masse)

    def display(self):
        
        fill(200)
        noStroke()
        circle(self.position.x, self.position.y, self.radius*2)
        #stroke(255,0,0)
        #line(self.position.x, self.position.y, self.position.x + self.acceleration.x*100, self.position.y + self.acceleration.y*100)
        


    def g(self, x):
       return  (x>=0)*x + 0
    
    def CheckOtherCollision(self):
        F = PVector(0,0)
        for other in bobs:
            if other.index != self.index:
                dij = (self.position - other.position).mag()
                nij = (self.position - other.position).normalize()
                rij = self.radius + other.radius 
                tij = nij.copy()
                tij.rotate(HALF_PI)
                stroke(255,0,0)
                #line(self.position.x, self.position.y, self.position.x + tij.x*30, self.position.y + tij.y*30)
                DeltaVij = (other.velocity - self.velocity).dot(tij)
                fij = (self.A*exp((rij - dij)/self.B)+self.k*self.g(rij - dij))*nij + (self.K*self.g(rij - dij)*DeltaVij)*tij
                F.add(fij)
        return F
    
            

    # def checkGroundCollision(self, grounds):
    #     F = PVector(0,0)
    #     for ground in grounds:
    #        if self.intersection(ground):
    #            self.velocity.y *=0.1 
    #            self.velocity.x *=0.1
    #            f = PVector(ground.b.x - ground.a.x, ground.b.y - ground.a.y,).rotate(HALF_PI)
    #            f.setMag(WallMag)
    #            F.add(f)
    #     return F
    
    
    
    def WallCollision(self, grounds):
        F = PVector(0,0)
        
        for ground in grounds:
             
            # définir un vecteur directeur de la droite du mur 
            v = ground.b - ground.a
            v.normalize()
            
            # definir les coordonnées du projeté orthogonal def projete(self, v)
            I = PVector(self.position.x - ground.x, self.position.y - ground.y)
            P = v.mult(v.dot(I))
            H = PVector(P.x + ground.x, P.y + ground.y)
            
            # déterminer la validité du projeté def isInSegment(x,y) 
            def isInSegment(H,ground):
                vA = ground.a - H
                vB = ground.b - H
                return vA.dot(vB)<=0
            
            # définir le vecteur normal, le vecteur tangent et appliquer la force 
            if isInSegment(H,ground):
                r = self.radius
                diw = (self.position - H).mag()
                n = (self.position - H).normalize()
                stroke(255,0,0)
                #line(H.x, H.y, H.x+n.x, H.y+n.y)
                t = n.copy().rotate(HALF_PI)
           
                
                fiw = (self.A*exp((r - diw)/self.B)+self.k*self.g(r - diw))*n + (self.K*self.g(r - diw)*(self.velocity.dot(t)))*t
                F.add(fiw)
        return F
    
    def FrictionForce(self):
        f = self.velocity.copy()
        f*= -friction * (self.velocity.mag())**2
        return f
            
            
    def FollowMouse(self):
         if mousePressed:
            ax = -(mouseX-self.position.x)
            ay = -(mouseY-self.position.y)
            return PVector(0,0)
         else:
            ax = mouseX-self.position.x
            ay = mouseY-self.position.y
            return PVector(ax,ay).setMag(MouseMag)
    
    def FollowObjective(self):
        if keyPressed:
            ax = self.obj.x - self.position.x
            ay = self.obj.y - self.position.y
            return PVector(ax,ay).setMag(ObjMag)
        else:
            return PVector(0,0)
    
    def FollowBarrier(self, barrier):
        F = PVector(0,0)
        if barrier.state == 'g':
            F = (PVector(vi,0)- self.velocity)/tau

            #F.mult(1/tau)
        return F
    def NeedForSpeed(self, barrier):
        F = PVector(0, 0)
        if barrier.state == 'g':
            F = (PVector(vi, 0) - self.velocity)/tau
        elif barrier.state == 'b':
            F = (PVector(-vi, 0) - self.velocity)/tau
        else:
            F = (PVector(0, 0) - self.velocity)/tau
        return F
         
    def intersection(self, ground):
         L = ground.a 
         E = ground.b 
         C = self.position  
         d = E.copy().sub(L) 
         r = self.radius 
         f = C.copy().sub(E)
         a = d.dot(d) 
         b = 2*f.dot(d) 
         c = f.dot(f) - r*r 
         delta  = b*b -4*a*c 
         t1 = (-b - sqrt(delta))/(2*a) 
         t2 = (-b + sqrt(delta))/(2*a) 
         T1 = E.copy().add(d.copy().mult(-t1)) 
         T2 = E.copy().add(d.copy().mult(-t2)) 
  
         return (delta > 0 and t1 >= 0 and t1 <= 1 or (t2 >= 0 and t2 <= 1))
     


class Ground(object):

    def __init__(self, x1, y1, x2, y2):
        self.a = PVector(x1, y1)
        self.b = PVector(x2, y2)
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        self.colour = (255,255,255)
        
    def update(self):
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        

class Barrier(Ground):
    
    def __init__(self, x1, y1, x2, y2):
        Ground.__init__(self, x1, y1, x2, y2)
        self.state = 'r'
        self.colour = (255,0,0)
        
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
            
        
