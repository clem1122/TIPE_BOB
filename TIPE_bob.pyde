bobs = []
grounds = []
nb_bobs = 25


def setup():
    size(640, 600)
    global grounds
    
    wall1 = Ground(100,300,300,100)
    wall2 = Ground(300,100,500, 300)
    wall3 = Ground(300,500,500, 300)
    wall4 = Ground(100,300,300,500)
    
    grounds = [wall1,wall2,wall3,wall4]
    
    for i in range(nb_bobs):
        bobs.append(Bob(random(250,300), random(250,300), 10,i))
    
    ellipseMode(RADIUS)
    
def draw():
    clear()
    noStroke()
    fill(0, 15)

    for bob in bobs:
        bob.move()
        bob.display()

    fill(127)
    beginShape()
    for ground in grounds:
        stroke(255)
        line(ground.a.x, ground.a.y, ground.b.x, ground.b.y)
        
        


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

    def move(self):
        self.acceleration.add(self.FollowMouse())
        self.acceleration.add(self.CheckOtherCollision())
        self.acceleration.limit(10)
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def display(self):
        # Draw orb.
        noStroke()
        fill(200)
        circle(self.position.x, self.position.y, self.radius)
        

    def checkGroundCollision(self, ground):
        
        # Get difference between orb and ground.
        deltaX = (self.position.x - ground.x)
        deltaY = (self.position.y - ground.y)

        # Precalculate trig values.
        cosine = cos(ground.rot)
        sine = sin(ground.rot)

        # Rotate ground and velocity to allow orthogonal collision.
        #  calculations
        groundXTemp = cosine * deltaX + sine * deltaY
        groundYTemp = cosine * deltaY - sine * deltaX
        velocityXTemp = cosine * self.velocity.x + sine * self.velocity.y
        velocityYTemp = cosine * self.velocity.y - sine * self.velocity.x
            
        # Ground collision - check for surface collision and also that orb is
        #  within left / right bounds of ground segment.
        
        if groundYTemp < 0:
            if (groundYTemp > -self.radius and
                self.position.x > ground.a.x and
                self.position.x < ground.b.x):
                # keep orb from going into ground.
                groundYTemp = -self.radius
                # bounce and slow down orb.
                velocityYTemp *= -1.0
                velocityYTemp *= Bob.Damping
        else:
            if (groundYTemp < self.radius and
                self.position.x > ground.a.x and
                self.position.x < ground.b.x):
                # keep orb from going into ground.
                groundYTemp = self.radius
                # bounce and slow down orb.
                velocityYTemp *= -1.0
                velocityYTemp *= Bob.Damping
    
        # Reset ground, velocity and orb.
        deltaX = cosine * groundXTemp - sine * groundYTemp
        deltaY = cosine * groundYTemp + sine * groundXTemp
        self.velocity.x = (cosine * velocityXTemp - sine * velocityYTemp)*0.9
        self.velocity.y = (cosine * velocityYTemp + sine * velocityXTemp)*0.9
        self.position.x = ground.x + deltaX
        self.position.y = ground.y + deltaY
        
    def CheckOtherCollision(self):
        F = PVector(0,0)
        for other in bobs:
            d = dist(other.position.x, other.position.y, self.position.x, self.position.y)
            if d != 0:
                f = PVector(ohter.x - self.x, other.y - self.y).normalize()
                f.mult(map(d, 0, 3 * self.radius, 10, 0))
                F.add(f)
                    
       return F
            
    def FollowMouse(self):
         if mousePressed:
            ax = -(mouseX-self.position.x)
            ay = -(mouseY-self.position.y)
        else:
            ax = mouseX-self.position.x
            ay = mouseY-self.position.y
        return PVector(ax,ay)
            
            
           
class Ground(object):

    def __init__(self, x1, y1, x2, y2):
        self.a = PVector(x1, y1)
        self.b = PVector(x2, y2)
        self.x = (self.a.x + self.b.x) / 2
        self.y = (self.a.y + self.b.y) / 2
        self.lon = dist(self.a.x, self.a.y, self.b.x, self.b.y)
        self.rot = atan2((self.b.y - self.a.y), (self.b.x - self.a.x))
        #bonjour
        


 
 
