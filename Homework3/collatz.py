def collatz(n):
    i = 1
    while(length(i) < n):
        i += 1
    return i

def math(i):
    if(i%2 == 1):
        i = (i*3)+1
    else:
        i = i / 2
    return i

def length(i):
    len = 0
    while(i != 1):
        i = math(i)
        len += 1
    return (len + 1)