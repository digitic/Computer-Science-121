def zap_buzz(x):
    if(x % 7 == 0):
        if(x % 10 == 3 or (x // 10) % 10 == 3 or (x // 100) % 10 == 3):
            return('zap buzz')
        else: 
            return('zap')
    elif(x % 10 == 3 or (x // 10) % 10 == 3 or (x // 100) % 10 == 3):
        return('buzz')
    else:
        return(x)