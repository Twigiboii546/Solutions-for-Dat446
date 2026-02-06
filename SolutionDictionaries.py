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

# Code words
def code_words(text, dictionary):
  words = text.split()
  new_text = []
  for i in words:
    if i in dictionary:
      new_text.append(dictionary[i])
    else:
      new_text.append(i)
  return " ".join(new_text)

# Histogram
def histogram(max_bar, labels, counts):
    max_count = max(counts.values())
    for label in labels:
        count = counts[label]
        num_stars = int(count / max_count * max_bar)
        print(label.ljust(10) + "*" * num_stars)

# Planet period
import math

# Constants
M = 1.991e30  # Mass of the sun in kg
G = 6.67e-11  # Gravitational constant in SI units

# Planet radii in meters
radii = {
  "mercury": 57.9e9,
  "venus": 108.2e9,
  "earth": 149.6e9,
  "mars": 228e9,
  "jupiter": 779.3e9,
  "saturn": 1427e9,
  "uranus": 2871e9,
  "neptune": 4497e9,
  "pluto": 5913e9
}

def planet_period(name):
  if name in radii:
    print(math.sqrt((4 * math.pi**2 * radii[name]**3) / (G*M)))
  else: 
    print("Unknown planet name")
