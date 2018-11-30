def fib3(n):
    prevPrev, prev, curr = 0,0,1
    i = 1
    while i < n:
        prevPrev, prev, curr = prev, curr, prevPrev + prev + curr
        i += 1
    return curr