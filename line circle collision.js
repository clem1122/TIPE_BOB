function setup() {
  L = createVector(100,100);
  E = createVector(100,200);
  C = createVector(150,150);
  d = E.copy().sub(L);
  
  r = 50;

  createCanvas(400, 400);
}

function draw() {
  f = C.copy().sub(E);
  C.x = mouseX;
  C.y = mouseY;
  a = d.dot(d);
  b = 2*f.dot(d);
  c = f.dot(f) - r*r;
  delta  = b*b -4*a*c;
  t1 = (-b - sqrt(delta))/(2*a);
  t2 = (-b + sqrt(delta))/(2*a);
  T1 = E.copy().add(d.copy().mult(-t1));
  T2 = E.copy().add(d.copy().mult(-t2));

  
  background(0);
  
  if(delta > 0 && t1 >= 0 && t1 <= 1 || (t2 >= 0 && t2 <= 1)  )
  {
    stroke(255,0,0);
  
    
  } else {
    stroke(255);
  }
  
  strokeWeight(2);
  point(L.x, L.y);
  point(E.x, E.y);
 
  noFill();
  circle(C.x, C.y, 2*r);
  lineV(L, E);
  
}

function lineV(a,b){
  line(a.x, a.y, b.x, b.y);
  

}
