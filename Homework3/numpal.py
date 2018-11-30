def digits(n):
    tempNum = n
    digitCount = 0
    while(tempNum >= 1):
        digitCount += 1
        tempNum = tempNum // 10
    return digitCount

def numpal(n):
    i = 0
    digCount = digits(n)
    while(digCount // 2 > i):
        if((n // (10 ** i)) % 10 != ((n // (10 ** (digCount - i - 1)) % 10))):
            return False
        i += 1
    return True