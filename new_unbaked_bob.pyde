bobs = []
grounds = []
nb_bobs = 140
MouseMag = 0.1
RepMag = 250
WallMag = 100
ObjMag = 20
frot = 0.8
bob_radius = 15
maxmasse = 95
R = 100
grounds = []
friction = 0.3
bob_damp = 0.8

nx = 100//(bob_radius+2)
ny = 320//(bob_radius+2)

x0 = (bob_radius+2)
y0 = (bob_radius+2)

savedlen = 500

j = 0


listPos = []
for i in range(nx):
    y0 = (bob_radius+2)
    x0 += (bob_radius+2)
    for j in range(ny):
        t = (x0,y0)
        listPos.append(t)
        y0 += (bob_radius+2)


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
    
    #bake()
    
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
    
    # for bob in bobs:
    
    #     pos = bob.savedpos[j]
    #     bob.display(pos.x, pos.y)

    # j = (j + 1) % savedlen
    
    fill(127)
    for ground in grounds:
        stroke(255)
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
    stroke(255)
    line(objectif.a.x, objectif.a.y, objectif.b.x, objectif.b.y)
    
    # if j < 10:
    #     t = "000" + str(i)
    # elif j < 100:
    #     t = "00" + str(i)
    # elif j < 1000: 
    #     t = "0" + str(i)   
    # else:
    #     t = str(j)
    # saveFrame("Frame/bobStory(" + t + ").png")
    
        
        
def bake():
    global objectif
    for i in range(savedlen):
        print(i*100/savedlen, " %")
        for bob in bobs:
            if bob.position.x<1200:
                bob.move(i)
            else:
                bob.position.x = 2*width
            
            bob.savepos()
        



class Bob(object):

    def __init__(self, x, y, radius, index):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        
        self.index = index
        self.obj = PVector(1200-3*radius,200)
        self.masse = random(60,95)
        self.radius = radius* self.masse/maxmasse
        self.savedpos = []

    def savepos(self):
        self.savedpos.append(self.position.copy())
        
    def move(self):
        self.velocity.add(self.acceleration)
        self.velocity.y*=frot
        #self.Reorient(grounds)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.CheckOtherCollision()
        self.acceleration.add(self.FollowObjective())

        self.acceleration.add(self.checkGroundCollision(grounds))
        self.acceleration.add(self.FrictionForce())
        self.acceleration.mult(1/self.masse)

    def display(self):
        noStroke()
        fill(200)
        circle(self.position.x, self.position.y, self.radius * 2)

    # def display(self, x, y):
    #     # Draw orb.
    #     noStroke()
    #     fill(200)
    #     circle(x, y, self.radius * 2)
        

    def checkGroundCollision(self, grounds):
        F = PVector(0,0)
        for ground in grounds:
           if self.intersection(ground):
               self.velocity.y *=0.1 
               self.velocity.x *=0.1
               #self.acceleration.y = 0
               f = PVector(ground.b.x - ground.a.x, ground.b.y - ground.a.y,).rotate(HALF_PI)
               f.setMag(WallMag)
               F.add(f)
        return F
    
    def FrictionForce(self):
        f = self.velocity.copy()
        f*= -friction * self.velocity.mag() 
        #f.setMag(friction)
        return f

    def CheckOtherCollision(self):
        for other in bobs[self.index:]:
            dP = PVector(other.position.x - self.position.x, other.position.y - self.position.y)
            d = other.radius + self.radius
            
            if self.position.dist(other.position) < d:
                angle = atan2(dP.y, dP.x) # pi/2 - angle de dP
                #angle = PVector.angleBetween(PVector(1,0),dP)

                T = PVector.fromAngle(angle)
                
                magnitude = map(self.position.dist(other.position), d, 1.5*d, 1, 0)
                T.setMag(d)
                
                A = T - dP
                A *= bob_damp#*magnitude

                
                self.velocity.sub(other.masse/(other.masse+self.masse)*A)
                other.velocity.add(self.masse/(other.masse+self.masse)*A)
        
            
            
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
        # if i > 0.5*savedlen:
        #     ax = self.obj.x - self.position.x
        #     ay = self.obj.y - self.position.y
        #     return PVector(ax,ay).setMag(ObjMag)
        # else:
        #     return PVector(0,0)
    
         
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
     

                        
     
     # next methods
     # def Reorient(self, grounds)
     # def isInDanger(self)
     # def watchPerimeter
     

#next function 
# def spawnDanger()

    
class Ground(object):

    def __init__(self, x1, y1, x2, y2):
        self.a = PVector(x1, y1)
        self.b = PVector(x2, y2)
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
