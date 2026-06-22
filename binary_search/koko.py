import math

piles = [1,4,3,2]
h = 9


def canFinish(k): 
    hours = 0
    for p in piles:
        hours += math.ceil(p / k)
    if hours <= h:
        return True
    return False


def minimumRate():
    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2

        if canFinish(mid):
            high = mid
        else:
            low = mid + 1
    return low

minimumRate()