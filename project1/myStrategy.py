def myStrategy(myscore, theirscore, last):
    if(myscore >= 97):
        if(myscore > theirscore):
            return 0
        elif(myscore > 98):
            return 0
        else:
            return 1
    if(myscore == 0):
        return 33
    #if(100 - myscore < myscore - (theirscore + 15)):
        #return 0
    if(last and myscore > theirscore):
        return 0
    else:
        return (((100 - myscore) // 2.95))