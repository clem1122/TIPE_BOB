bobs = []
grounds = []
nb_bobs = 70
MouseMag = 0.1
RepMag = 3*50
WallMag = 6*50
ObjMag = 0.05*40
frot = 0.85
bob_radius = 20
maxmasse = 95
grounds = []


h = 400
w = 1400
pression_field = [0]*h
for i in range(len(pression_field)):
    pression_field[i] = [0]*w
    
    

def setup():
    size(1400, 400, P3D)
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
        bobs.append(Bob(random(35,45), random(55,320), bob_radius,i))
    
    #ellipseMode(RADIUS)
    
def draw():
    global objectif
    objectif = Ground(1200,370,1200,30)
    
    clear()
    noStroke()
    fill(0, 15)
    wall1 = grounds[0]

    for bob in bobs:
        if bob.position.x<objectif.x:
            bob.move()
            bob.display()
        else:
            bobs.remove(bob)
        

    fill(127)
    beginShape()
    for ground in grounds:
        stroke(255)
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
    


    


class Bob(object):

    def __init__(self, x, y, radius, index):
        self.position = PVector(x, y)
        self.velocity = PVector(0.1, 0)
        self.acceleration = PVector(0,0)
        
        self.index = index
        self.obj = PVector(1200-3*radius,200)
        self.masse = random(45,95)
        self.radius = radius* self.masse/maxmasse

    def move(self):
        #self.acceleration.limit(1)
        self.velocity.add(self.acceleration)
        self.velocity.y*=frot
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.acceleration.add(self.CheckOtherCollision())
        #self.acceleration.add(self.FollowMouse())
        self.acceleration.add(self.FollowObjective())
        self.acceleration.add(self.checkGroundCollision(grounds))
        self.acceleration.mult(1/self.masse)

    def display(self):
        # Draw orb.
        noStroke()
        fill(200)
        circle(self.position.x, self.position.y, self.radius * 2)
        

    def checkGroundCollision(self, grounds):
        F = PVector(0,0)
        for ground in grounds:
           if self.intersection(ground):
               f = PVector(ground.b.x - ground.a.x, ground.b.y - ground.a.y,).rotate(HALF_PI)
               f.setMag(WallMag)
               F.add(f)
               f.normalize()
               x = ceil(self.position.x)
               y = ceil(self.position.y)
               pression = abs(self.masse * self.acceleration.dot(f) / (PI*self.radius**2))
               print(pression)
               pression_field[y][x] += pression
        return F
 
        
    def CheckOtherCollision(self):
        noFill()
        stroke(255)        
        F = PVector(0,0)
        for other in bobs:
            d = dist(other.position.x, other.position.y, self.position.x, self.position.y)
            if d  < self.radius*1.5 and d > 0:
                f = PVector(self.position.x - other.position.x, self.position.y - other.position.y)
                f.setMag(map(d, 0, 1.5*self.radius**2, RepMag, 0))
                F.add(f)
                
                    
        return F
            
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
        ax = self.obj.x - self.position.x
        ay = self.obj.y - self.position.y
        return PVector(ax,ay).setMag(ObjMag)


        
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
