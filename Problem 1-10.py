## Problem 1 ##
vec = []                                   # Create empty vector
for i in range(1,1000):                    # Loop 1k times without zero
    if (i % 3 == 0) | (i % 5 == 0) :       # If i in 1,2,3...,1000 is evenly divisible by 3 or 5 then store these nrs
        vec.append(i)       
sum(vec) 

## Problem 2 ##
i = 1                                      # Start i at 1
vec = []                                   # Create empty vector to store all sequences in
while i < 4000000 :                        # As long as i is under 4Mil then loop
    for j in range(0,32) :                 # Use for loop to select value one step before i in stored vector
     vec.append(i)                         # Save fibonacci sequence in vector
     i = i + vec[j - 1]                    # Update i to be its current value plus value one step before

vec2 = []                                  # Create new vector for storing even nr in previous vector
for k in vec :                             # Loop directly from previous vector
    if k % 2 == 0 :                        # If an element is evenly divisible then store it in new vector
        vec2.append(k)
sum(vec2)

## Problem 3 ##
targetprime = 600851475143                 # State target prime nr
testvec = list(range(1,7000))              # Create arbitrary large vector of values 1,2,3...,7k to divide targetprime
vec = []                                   # Create empty vector for storage 
for i in testvec:
    if targetprime % i == 0 :              # For i to be a factor of the targetprime it must evenly divide 
        vec.append(i)

max(vec)

## Problem 4 ##
Range = np.arange(900,999)                 # Only use most upper combinations (start with 900 since need 3 digit nr)
vec ,v  = [], []                           # Create empy vectors to store iterations
for i in Range:                            # We need all combinations of multiple values between 900 to 999
    for j in Range:                        # This takes 900 and multiplies it with 900 to 999 then 901 and multiplies with 900 to 999 (may be small amount of duplicates)
        itr = i*j                          # Store the multiples in variable to then store in vec, easier in R
        vec.append(itr)

for k in np.sort(vec[round(len(vec)/2) : len(vec)-1]):    # Now that we have all combinations, use last half max values to search for palindromes
    if (str(k)[0] == str(k)[5]) & (str(k)[1] == str(k)[4]) & (str(k)[2] == str(k)[3]) : # If first and last digit is same & second digit and second last digit is same ... its a palindrome (note all nr in last 100k in vector have 6 digits)
        v.append(k)
max(v)

## Problem 5 ##
def MultiDiv(start, finish, lst):
    def Div(n, lst):
        return all(map(lambda y: n % y == 0, lst))        # Create a subfunction which only returns True/False if a singe nr is evenly 
                                                          # divisible by a given long list of nr - much like n%1==0 & n%2==0 & n%3==0 ...
    for i in range(start, finish, 2):                     # Only range for even numbers since uneven numbers can never by evenly divided by even numbers
        if Div(i, lst) == True:                           # The long list of only positive integers will check if it is evely divisible by the given list
            print(i)                                      # If Div() returns True then the specific nr is evenly divisible by the whole given list
                                                                       
MultiDiv(220000000,300000000, [3,5,7,9,11,13,15,17,19])      
# By using a separate function to find logical values (if evenly divisible by all nrs) 
# and then to use it in a new loop with high ranges to see if True then print that number
# reduces time complexity severely compared to using a for loop to see if each nr
# within the large range is divisible by 2 & 3 & 4 & 5 ... & 20, from 2.23min to 3.2sec

## Problem 6 ##
sequence = np.arange(1,101)
sqrdsum = sum(sequence)**2
sumsqrd = sum(sequence**2)
sqrdsum - sumsqrd

## Problem 7 ##
vec = []
itr = 2
# Start while-loop with 2, and when itr=2 then inner for-loop is i=[] and if 2%[]==0 (which by default it isnt) then it breaks and SAVES.
# Next, itr=3 then inner loop i=[2] and if 3%2==0 (which it isnt) then it breaks and SAVES.
# Next, itr=4 then inner loop i=[2,3] and if 4%2==0 (which it is) or 4%3==0 (which it isnt) then it breaks.
# This is because 2x2=4 so 4 is composite number NOT prime and so on. This continues such that last iteration itr=149999
# is checked if 149999%[2,3,4,5...149998]==0 (NEVER CHECK FOR 1 Or ITSELF) to not save composite numbers, compisite numbers appear often as numbers gets larger
while itr < 150000:
    for i in range(2,itr):
        if itr % i == 0:
            break
    else: vec.append(itr)
    itr = itr + 1

vec[10001-1]

## Problem 8 ## 
import math                                        # Must import math since np.prod() does not give large enough product as math.prod()
largenr = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

vec, vec2 = [] , []                                 # Create two empty vectors for loop

for i in range(0,len(largenr)-13):                  # Since we move 13 characters 1 step at a time, the first 13 charachters are in the first step. It iterates then through 1000-13 steps.
        vec.append(largenr[i:i+13])                 # Starts at position 0 to 0+13 then 1 to 1+13 so it moves a 13 length vector over each characters in string.

for j in vec:                                       # Now that all 13 adjacent digit combinations are found, lets store their product and see the largest product
    vec2.append(math.prod(list(map(int, str(int(j))))))     # '123' must be split into '1' '2' '3' and then into ['1','2','3'] to get 1*2*3

max(vec2)

## Problem 9 ##
vec = []
for a in range(1,450):                              # Use 3 nested loops to find all combinations of 3 digits. Only have to use up until 500 since a^2+b^2 must be c^2
    for b in range(1,450):                          # First loop gives 1 1 1 second 1 1 2 then 1 1 3 up until 450 450 450
        for c in range(1,450):                      # However there might be many duplicates - 20 19 200 and 200 19 20 or likewise
            if (a < b < c):                         # since their sum is the same. Then only save if a<b<c which reduces complexity
                vec.append([a,b,c])

for i in range(0,len(vec)):                         # Now if a^2+b^2-c^2 = 0 & a+b+c=1000 then the criterias are met. Use these logical
    if ((vec[i][0]**2 + vec[i][1]**2 - vec[i][2]**2) == 0) & ((vec[i][0] + vec[i][1] + vec[i][2]) == 1000): # criterias within this separate loop to cut time complexity from 34sek to 29sek
        print(vec[i][0], vec[i][1], vec[i][2])
        
## Problem 10 ##
vec = []
itr = 2
# This is reused code for finding all consecutive primes, find all below 2 mil
while itr < 2000000:
    for i in range(2,itr):
        if itr % i == 0:
            break
    else: vec.append(itr)
    itr = itr + 1
# Then sum all those primes 2+3+5+7+11...+1999993. It takes time, but answer is 142913828922
sum(vec) 
