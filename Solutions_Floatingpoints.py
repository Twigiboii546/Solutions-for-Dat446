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
#Basel problem ran this instead it worked alot better
def basel(epsilon):
    n = 1
    s = 0.0
    while 1 / (n * n) >= epsilon:
        s += 1 / (n * n)
        n += 1
    return s
# extrapolate just use the formula
def extrapolate(x1,y1,x2,y2,x):
  y= float(((y2-y1)*x/(x2-x1))+((y1*x2)-(y2*x1))/(x2-x1))
  return y
# Tip make sure your fucking formatting is right and dont blame logic directly :(
def calculate_loan(property_price, loan, interest_rate):
    ratio = loan / property_price

    amort_rate = 0.0
    if ratio >= 0.70:
        amort_rate = 0.02
    elif ratio >= 0.50:
        amort_rate = 0.01

    monthly_amortization = loan * amort_rate / 12
    monthly_interest = loan * (interest_rate / 100) / 12

    print("amortization:",monthly_amortization)
    print("interest:",monthly_interest)
    print("total:",monthly_amortization + monthly_interest)

#escape speed 
def escape(M, r, V):
  G = 6.674*10**(-11)
  ve = math.sqrt(2*G*M/r)
  if V>ve:
    vinf= math.sqrt((V**2)-(ve**2))
  else:
    vinf= math.sqrt(-(V**2)+(ve**2))
  if(vinf > ve):
    print("Excess speed:",vinf)
  else:
    print("the object won't escape")


def cube_root(r, epsilon):
  xn=float(1.0)
  iteration = 0
  ratio=float(10.0)
  while ratio > epsilon:
    print("Iteration",iteration,":",xn)
    xn1=float((1/3)*((2*xn)+(r/xn**2)))
    print(xn1,xn)
    iteration += 1
    if(xn > xn1):
      ratio=xn-xn1
    else:
      ratio=xn1-xn
    xn=xn1
  pass
# newton jadajada method
def cube_root(r, epsilon):
    xn = 1.0
    iteration = 0

    while True:
        print("Iteration", iteration, ":", xn)

        xn1 = (1/3) * (2*xn + r/(xn**2))

        if abs(xn1 - xn) < epsilon:
            break

        xn = xn1
        iteration += 1
pass


# elo calculator
def guess_winner(white_rating, black_rating):
  #elo is the worst fucking thing ever

  score= 1/(1+10**((white_rating-black_rating)/400))
  if(score>=0.55):
    print("Black is expected to win")
  if(score <= 0.45):
    print("White is expected to win")
  if(score > 0.45 and score < 0.55):
    print("A draw is expected")
            

# NB. tests only check that you output correct numbers, 4 decimals


