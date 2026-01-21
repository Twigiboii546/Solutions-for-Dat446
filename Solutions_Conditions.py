def going_out(sunny, meeting):
  if sunny == True and meeting == False:
    return True
  else: 
    return False
  ## age
def legal_status(age):
  if age < 18:
    return "minor"
  if age >= 18 and age < 21:
    return "adult"
  if age >= 21 and age < 30:
    return "alcohol"
  if age >= 30 and age < 35:
    return "senator"
  if age >= 35:
    return "president"
  ##
  def near_number(m,n):
    if abs(n-m) <= 10:
      return True
    else:
      return False
# Grades blud    
def grades(n):
  grades_letters = ["F","F","D","C","B","A"]
  return grades_letters[n]

## grades 100
def grades(n):
  grades_letters = ["A","B","C","D","F"]
  if n >= 90:
    return grades_letters[0]
  if n >= 80 and n < 90:
    return grades_letters[1]
  if n >= 70 and n < 80:
    return grades_letters[2]
  if n >= 60 and n < 70:
    return grades_letters[3]
  else:
    return grades_letters[4]
## movietickets
def movieTickets(nrTickets,nrUnder18,time):
  price = ((nrTickets-nrUnder18)*100) + (nrUnder18*50)
  if time >= 18:
    return price
  else:
    return price*0.90
## Pandemic shit
def pandemic_rules(numC, totalNum, population):
  ratio = totalNum/(population/100000)
  if ratio >= 50 and ratio > numC:
    return "red"
  if ratio >= 25 and ratio < 50 and ratio > numC:
    return "yellow"
  if ratio <= 25:
    return "green"
  if ratio > numC:
    return "green"
  else:
    return "green"
  


 ## Code of the rugby match
def main():
  tries = int(input("Number of tries"))
  #print(tries)
  conversions = int(input("Number of conversions"))
  #print(conversions)
  if conversions > tries:
    print("Impossible: too many conversions or too few tries.")
    
  penalties = 0
  drop_goals = 0
  if conversions <= tries:
    penalties = int(input("Number of penalties"))
    #print(penalties)
    drop_goals = int(input("Number of drop goals"))
    #print(drop_goals)
    points = (tries*5)+(conversions*2)+(penalties*3)+(drop_goals*3)
    print("Game points:",points)
  
  pass
# Code for the flowersale
def calculate_flower_price(flower_count, week_number):
  price= flower_count*20
  if week_number >= 14 and week_number <= 17:
    if flower_count % 2 == 0:
      price = price/2
    else:
      price = (price + 20)/2
  else:
    if flower_count >= 200:
      price =price *0.8
  return int(price)
  pass  # Implement this logic
  


def main():
  flower_count = int(input("Enter the amount of flowers?"))
  week_number = int(input("Enter what week?"))
  print("The price is",calculate_flower_price(flower_count, week_number))
  
  # read input data
  # use calculate_flower_price to do the computation
  # print the result
  pass

 


#print(movieTickets(5,3,17))
print(pandemic_rules(10,350,1000000))
  

