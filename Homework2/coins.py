def coins(x):
    coinCount = 0
    while(x >= 25):
        x -= 25
        coinCount += 1
    while(x >= 10):
        x -= 10
        coinCount += 1
    while(x >= 5):
        x -= 5
        coinCount += 1
    while(x >= 1):
        x -= 1
        coinCount += 1
    return(coinCount)