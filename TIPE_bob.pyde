
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
        # Move orb.
        if mousePressed:
            ax = -(mouseX-self.position.x)
            ay = -(mouseY-self.position.y)
        else:
            ax = mouseX-self.position.x
            ay = mouseY-self.position.y
        self.acceleration = PVector(ax, ay)
        self.acceleration.normalize()
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        

    def display(self):
        # Draw orb.
        noStroke()
        fill(200)
        circle(self.position.x, self.position.y, self.radius)

    # Check boundaries of window.
    def checkWallCollision(self):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -Bob.Damping

        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -Bob.Damping

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
                self.position.x > ground.x1 and
                self.position.x < ground.x2):
                # keep orb from going into ground.
                groundYTemp = -self.radius
                # bounce and slow down orb.
                velocityYTemp *= -1.0
                velocityYTemp *= Bob.Damping
        else:
            if (groundYTemp < self.radius and
                self.position.x > ground.x1 and
                self.position.x < ground.x2):
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
        
    def checkOtherCollision(self):
        for other in bobs[self.index:]:
            dx = other.position.x - self.position.x
            dy = other.position.y - self.position.y
            minDist = other.radius + self.radius
            if self.position.dist(other.position) < 1.1*minDist:
                angle = atan2(dy, dx)
                targetX = self.position.x + cos(angle) * minDist
                targetY = self.position.y + sin(angle) * minDist
                ax = (targetX - other.position.x) * Bob.Spring
                ay = (targetY - other.position.y) * Bob.Spring
                self.velocity.x -= ax
                self.velocity.y -= ay
                other.velocity.x += ax
                other.velocity.y += ay

class Ground(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = (self.x1 + self.x2) / 2
        self.y = (self.y1 + self.y2) / 2
        self.length = dist(self.x1, self.y1, self.x2, self.y2)
        self.rot = atan2((self.y2 - self.y1), (self.x2 - self.x1))
        
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
 
 
global obj
obj = (100,300)
def draw():
    clear()

    noStroke()
    fill(0, 15)
    rect(0, 0, width, height)

    for bob in bobs:
        
        for ground in grounds:
            bob.checkGroundCollision(ground)
        bob.checkOtherCollision()
        bob.checkWallCollision()
        bob.move()
        bob.display()

    fill(127)
    beginShape()
    for ground in grounds:
        stroke(255)
        line(ground.x1, ground.y1, ground.x2, ground.y2)