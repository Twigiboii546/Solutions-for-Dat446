#logisticsmap Revisited
def logmap(r,x):
  #writing for logmanp
  return r*x*(1-x)
  pass

def experiment(r,x):
  Xnew=x
  while True:
    yield(Xnew)
    Xnew=logmap(r,Xnew)
  pass

def table(r,x0,y0):
  x1new=x0
  x2new=y0
  while True:
    yield (x1new,x2new)
    x1new=logmap(r,x1new)
    x2new=logmap(r,x2new)
  pass
#first items yielded

def take_n(n,gen):
  gen =iter(gen)
  items = []
  for _ in range(n):
    try:
      items.append(next(gen))
    except StopIteration:
      break
  return items



#searching incomplete
def find_subsequence(sub,seq):
  indicies = []
  for i in range(len(seq)-len(sub)+1):
    if seq[i:i+len(sub)] == sub:
      yield i
  return 
