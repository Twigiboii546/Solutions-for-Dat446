import math 


# Cylinder shit
def cylinder_area(r,h):
  area = float(circle_circumference(r)*h + circle_area(r)*2)
  return area
def circle_area(r):
 area = float(math.pow(r,2)*math.pi)
 return area

def circle_circumference(r):
  circumferance = float(2*math.pi*r)
  return circumferance


import math
def shell_volume(r, R):
  volume = float((4/3) * math.pi*(math.pow(R,3) - math.pow(r,3)))
  return volume
  pass  # Implement this logic

def main():
  inner_r = float(input("Inner radius (m)?"))
  outer_r = float(input("Outer radius (m)?"))
  density = float(input("Density (kg/m³)?"))
  print("Volume:",shell_volume(inner_r, outer_r),"m³")
  print("Mass:",shell_volume(inner_r, outer_r)*density,"kg")
  
  # read input
  # compute results, using any helper functions you need
  # print the results
  pass

import math
def basel(epsilon):
  n=1
  argument = float(math.pow(math.pi,2)/6)
  answere = 0
  while argument-answere > epsilon:
    answere += float(1/math.pow(n,2))
    n += 1
  return answere
# NB. tests only check that you output correct numbers, 4 decimals


