def poly2max(x1, x2, y1, y2):
    xCount = x1
    z = -100000000
    while(xCount <= x2):
        yCount = y1
        while(yCount <= y2):
            tempEq = -xCount**4 + 3*xCount**2 - yCount**4 + 5*yCount**2
            if(tempEq > z):
                z = tempEq
            yCount += 1
        xCount += 1
    return int(z)