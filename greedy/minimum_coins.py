


min_coins = 0

total_sum = 25

curr_sum = 0

while curr_sum < total_sum:
    diff = total_sum - curr_sum
    if diff >= 20:
        curr_sum += 20
    elif diff >= 10:
        curr_sum += 10
    else:
        curr_sum += 5
    min_coins += 1

print(min_coins)