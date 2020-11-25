bobs = []
grounds = []
nb_bobs = 500
MouseMag = 0.1
RepMag = 1
WallMag = 5
frot = 0.975
bob_radius = 5
grounds = []
savedlen = 300

i = 0

def setup():
    size(1400, 400, P3D)
    global grounds
    
    up1 = Ground(0,30,400,30)
    up2 = Ground(400,30,520,120)
    up3 = Ground(520, 120,620,120)
    up4 = Ground(620,120,740,30)
    up5 = Ground(740,30,1110,30)
    
    dn5 = Ground(1110,370,740,370)
    dn4 = Ground(740,370,620,280)
    dn3 = Ground(620,280,520,280)
    dn2 = Ground(520,280,400,370)
    dn1 = Ground(400,370,0,370)
    
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
    
    grounds.append(depart)
    grounds.append(objectif)
    
    for i in range(nb_bobs):
        bobs.append(Bob(random(30,60), random(60,340), bob_radius,i))
    
    bake()
    #ellipseMode(RADIUS)
    
def draw():
    global i
    clear()
    noStroke()
    fill(0, 15)
    
    for bob in bobs:
    
        pos = bob.savedpos[i]
        bob.display(pos.x, pos.y)

    i = (i + 1) % savedlen
 

    fill(127)
    for ground in grounds:
        stroke(255)
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
    
    if i < 10:
        t = "000" + str(i)
    elif i < 100:
        t = "00" + str(i)
    elif i < 1000: 
        t = "0" + str(i)   
    else:
        t = str(i)
    saveFrame("Frame/bobStory(" + t + ").png")
    
        
        
def bake():
    for i in range(savedlen):
        print(i*100/savedlen, " %")
        for bob in bobs:
            bob.move()
            
            bob.savepos()

        

class Bob(object):
    # A damping of 80% slows it down when it hits the ground.
    Damping = 0.1
    Spring = 0.8

    Friction = -1

    def __init__(self, x, y, radius, index):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0,0)
        self.radius = radius
        self.index = index
        self.savedpos = []

    def move(self):

        
        #self.acceleration.limit(1)
        self.velocity.add(self.acceleration)
        self.velocity.mult(frot)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.acceleration.add(self.CheckOtherCollision())
        self.acceleration.add(self.FollowMouse())
        self.acceleration.add(self.checkGroundCollision(grounds))

    def savepos(self):
        self.savedpos.append(self.position.copy())
        
    
    
    def display(self, x, y):
        # Draw orb.
        noStroke()
        fill(200)
        circle(x, y, self.radius * 2)
        

    def checkGroundCollision(self, grounds):
        F = PVector(0,0)
        for ground in grounds:
           if self.intersection(ground):
               f = PVector(ground.b.x - ground.a.x, ground.b.y - ground.a.y,).rotate(HALF_PI)
               f.setMag(WallMag)
               F.add(f)
        return F
 
        
    def CheckOtherCollision(self):
        noFill()
        stroke(255)        
        F = PVector(0,0)
        for other in bobs:
            d = dist(other.position.x, other.position.y, self.position.x, self.position.y)
            if d  < self.radius*3 and d > 0:
                f = PVector(self.position.x - other.position.x, self.position.y - other.position.y)
                f.setMag(map(d, 0, 3*self.radius, RepMag, 0))
                F.add(f)
                    
        return F
            
    def FollowMouse(self):
         if mousePressed:
            ax = -(width-self.position.x)
            ay = -(height/2-self.position.y)
            return PVector(0,0)
         else:
            ax = width-self.position.x
            ay = height/2-self.position.y
            return PVector(ax,ay).setMag(MouseMag)
            
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
