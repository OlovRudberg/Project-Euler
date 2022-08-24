## Problem 12 ##
def Triangular(limit):                         # First build function which spits out triangle nrs, choose sizeable limit
    vec = []
    itr = 1 
    new = 0 
    while itr < limit:                         # First iteration itr=1 new=0 save new, second itr=2 new=1+0 save new, third itr=3 new=2+1 save new, fourth itr=4 new=3+3 save new...
        vec.append(new) 
        new = itr + new 
        itr = itr + 1
    return(vec)

def Divisor(n):                                # Build a fast computational function which returns all nrs that divides n
    div = [] 
    for i in range(1,round(n**0.5) + 1):       # We only need to look for divisors 1 to sqrt(n) + 1 since largest factorization is itself times itself
        if n % i == 0:                         # However we need to check for composite divisors which is the quotient of n % i, so we must store both i and n/i
            div.append([i,n/i])                # Number theory helps us to not have to search all n possibilities but only sqrt(n) + 1
    protract = sum(div,[])                     # Flatten 2D array and sort
    protract.sort()
    return(protract)

for i in Triangular(50000):                    # Just plug in all triangle nrs iterably until a nr which yields > 500 divisors
    if len(Divisor(i)) >= 500:
        print(i)
        break
