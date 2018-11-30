def solve(a,b,c):
    #Assigning discriminant, the square root of it, and the two possible solutions.
    eqBit = b**2 - 4*a*c
    sqRt = squareRoot(eqBit)
    firstSol = ((-b + sqRt) // (2*a))
    secondSol = ((-b - sqRt) // (2*a))
    #print("First solution remainder? " + str((-b + sqRt) % (2*a)))
    #print("Second solution remainder? " + str((-b - sqRt) % (2*a)))
    #Check for negative discriminant.
    if(eqBit < 0):
        #print("Negative Discriminant.")
        return False
    #Check for zero discriminant.
    elif(eqBit == 0):
        return firstSol
    #Check for if the discriminant is not a perfect square.
    elif(sqRt == -1):
        #print("Not a perfect square.")
        return False
    #Check for if -b + or - sqRt is not evenly divisible by 2*a
    elif((((-b + sqRt) % (2*a)) != 0) and (((-b - sqRt) % (2*a)) != 0)):
        #print("Remainder after dividing.")
        #print("First Solution: " + str(firstSol))
        #print("Second Solution: " + str(secondSol))
        return False
    #If the solutions are different, integers, and both exist:
    else:
        if(firstSol > secondSol):
            if(((-b + sqRt) % (2*a)) == 0):
                return firstSol
            else:
                return secondSol
        else:
            if(((-b - sqRt) % (2*a)) == 0):
                return secondSol
            else:
                return firstSol

def squareRoot(n):
    i = 0
    while(i <= n):
        if(i*i == n):
            return i
        i += 1
    return -1