coins = [1, 2, 5]

amount = 100


def answer():
    minimum = 1000000


    def backtrack(total, path):
        nonlocal minimum
        if total == amount:
            minimum = min(minimum, path)
            return
        elif total > amount:
            return
        
        for coin in coins:
            backtrack(total+coin, path + 1)
    return minimum

print(answer())