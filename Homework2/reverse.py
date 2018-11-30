def reverse(x):
    dig1 = x % 10
    dig2 = (x // 10) % 10
    dig3 = (x // 100) % 10
    return (dig1 * 100) + (dig2 * 10) + dig3