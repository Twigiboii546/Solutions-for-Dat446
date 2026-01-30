#greeting
def greeting(name):
  txt=f"Hello, {name}!!!"
  return txt
#tags
def tag(style, text):
  fintxt=f"<{style}>{text}</{style}>"
  return fintxt
#numerology
def numeric_value(text):
  textlowerd = text.lower()
  sum =0
  alpabet="abcdefghijklmnopqrstuvwxyz"
  for i in range(len(text)):
    current = 0
    for j in range(len(alpabet)):
      if textlowerd[i] == alpabet[j]:
        current += j+1
    sum += current
    current=0
  return sum
#same ends
def same_ends(seq):
  if len(seq)==0:
    return False
  if seq[0] == seq[len(seq)-1]:
    return True
  else:
    return False
#swap
def swap(list):
  newlist = list[int(len(list)/2):]+list[:int(len(list)/2)]
  return newlist

#skip
def skip(list,n):
  newlist = []
  for i in range(len(list)):
    if i % n == 0:
      newlist.append(list[i])
  return newlist  
#print(skip(["A","B","C","D","E"],2))
#print(skip([1,2,3,4,5,6,7],3),)
#Acronym
def acronym(text):
  newtext = text[0]
  for i in range(len(text)):
    if text[i] == " ":
      newtext += text[i+1]
  return newtext.upper()
print(acronym("random access memory"))
# caesar encryption
def caesar(n,text):
  alphabet ="abcdefghijklmnopqrstuvwxyz"
  loweredtext =  text.lower()
  newtext=""
  for i in range(len(text)):
    for k in range(len(alphabet)):
      if loweredtext[i]==alphabet[k]:
        try:
            newtext += alphabet[k+n]
        except:
          if k+n > len(alphabet):
            newtext += alphabet[k+n-len(alphabet)]
  return newtext
#print(caesar(2,"secret"))
#print(caesar(4,"yield"))
# add vectors
def add_vectors(a,b):
  result = []
  for i in range(len(a)):
    result.append(a[i]+b[i])
  return tuple(result)
  
print(add_vectors((3,3),(2,-1)))
#divisible by nine
#Not complete
def div9(num):
  while True:
    snum = str(num)
    print(snum)
    temps= ""
    if len(snum) == 1:
      break
    for i in range(len(num)):
      
  if int(snum) % 9 == 0:
    return True
