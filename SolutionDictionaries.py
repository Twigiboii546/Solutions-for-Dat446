# kcals
def kcals(a,b):
  price = 0
  for loop, product in b:
    price += loop * a[product]
  return price

# Word index (lite goofy men funkar)
def word_index(input):
  words = input.split()
  index_dict = {}
  for i in range(len(words)):
    word = words[i]
    if word in index_dict:
      index_dict[word].append(i)
    else:
      index_dict[word] = [i]
  return(index_dict)