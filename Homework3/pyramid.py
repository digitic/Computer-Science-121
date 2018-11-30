def pyramid(h):
    i = 1
    ret = ""
    while(i <= h):
        ret += (" " * (h-i))
        ret += ("* " * (i-1))
        ret += ("*\n")
        i += 1
    return ret