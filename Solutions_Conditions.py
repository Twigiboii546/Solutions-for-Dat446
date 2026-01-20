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


#print(movieTickets(5,3,17))
print(pandemic_rules(10,350,1000000))
  

