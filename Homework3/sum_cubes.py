def sum_cubes(n):
    i = 1
    total = 0
    while(i <= n):
        total += i*i*i
        i += 1
    return total