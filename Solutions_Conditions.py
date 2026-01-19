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

