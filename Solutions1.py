#First assigments not added

# Factorial
def factorial (n):
    sum = 1
    i=1
    for i in range(n):
        sum=sum*(i+1)
    print(sum)
    return sum

# Harmonic sum
def hSum (n):
    sum = 0
    for i in range(n):
        sum += (1/(i+1))
    print(sum)
    return sum
# guitarfrequency
def guitarfrequency(L, v):
    f = v/(2*L)
    print(f)
    return f
# Animal life
def human_years(pet_age,pet_lifespan, humanlifespan):
    
    human_age = (pet_age*humanlifespan)/pet_lifespan
    
    if human_age - int(human_age) >= 0.5:
        print(int(human_age)+1)
        return int(human_age)+1
        
    else:
        print(int(human_age))
        return int(human_age)

# Running ground
#factorial(5)
#hsum(5)
#guitarfrequency(0.8, 425)
human_years(17,200,100)