def max_of_two(f1, f2, n):
    sol1 = f1(n)
    sol2 = f2(n)
    if(sol1 >= sol2):
        return sol1
    else:
        return sol2