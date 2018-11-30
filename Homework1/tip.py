#Getting all the input values.
dollar = int(input("Price dollars? "))
cents = int(input("Price cents? "))
tip = int(input("Tip percentage? "))
#Calculating the price in cents and finding the tip in cents.
totalCents = (dollar * 100) + cents
tipCents = totalCents * (tip / 100.0)
#Returning the tip in dollar/cent format.
print(tipCents / 100.0)