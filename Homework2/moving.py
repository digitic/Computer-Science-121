def cheapest(x):
    aliceTrips = x // 11
    if(x % 11 > 0):
        aliceTrips += 1
    bobTrips = x // 14
    if(x % 14 > 0):
        bobTrips += 1
    alice = aliceTrips * 200
    bob = bobTrips * 250
    if(alice < bob):
        return('Alice')
    else:
        return('Bob')