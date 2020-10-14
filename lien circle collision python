def intersection(self, ground):
  L = PVector(100,100) 
  E = PVector(100,200) 
  C = PVector(150,150) 
  d = E.copy().sub(L) 
  r = 50 
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
