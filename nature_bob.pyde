bobs = []
grounds = []
nb_bobs = 30
MouseMag = 0.1
RepMag = 250
WallMag = 100
ObjMag = 20
frot = 0.97
bob_radius = 20
maxmasse = 95
R = 100
grounds = []
friction = 0.27
bob_damp = 0.8

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
    
    objectif = Ground(1200,370,1200,30)
    
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
    #grounds.append(objectif)
    
    for i in range(nb_bobs):
        bobs.append(Bob(random(10,380), random(110,310), bob_radius,i))
    
    
def draw():
    global objectif
    global j
    objectif = Ground(1200,370,1200,30)
    

    clear()
    noStroke()
    fill(0, 15)
    #wall1 = grounds[0]

    for bob in bobs:
        if bob.position.x<objectif.x:
            bob.move()
            bob.display()
        else:
            bob.position.x = 5 #2*width
    
    fill(127)
    for ground in grounds:
        stroke(255)
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
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
        
        self.A = 10
        self.B = 7
        self.k = 35
        self.K = 10
        
        
    def move(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.acceleration.add(self.CheckOtherCollision())
        self.acceleration.add(self.FollowObjective())
        self.acceleration.add(self.checkGroundCollision(grounds))
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
                tij = nij.copy().rotate(HALF_PI)
                DeltaVij = (other.velocity - self.velocity).dot(tij)
                fij = (self.A*exp((rij - dij)/self.B)+self.k*self.g(rij - dij))*nij + (self.K*self.g(rij - dij)*DeltaVij)*tij
                F.add(fij)
        return F
    
            

    def checkGroundCollision(self, grounds):
        F = PVector(0,0)
        for ground in grounds:
           if self.intersection(ground):
               self.velocity.y *=0.1 
               self.velocity.x *=0.1
               f = PVector(ground.b.x - ground.a.x, ground.b.y - ground.a.y,).rotate(HALF_PI)
               f.setMag(WallMag)
               F.add(f)
        return F
    
    def FrictionForce(self):
        f = self.velocity.copy()
        f*= -friction * self.velocity.mag() 
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
