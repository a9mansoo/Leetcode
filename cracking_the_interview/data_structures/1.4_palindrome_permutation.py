# A palindrome is symetric, each character has a pair
# Count how many have odd frequencies

from collections import Counter


def sol_1(s):
    new_s = "".join([new_char.lower() for new_char in s if new_char != " "])
    counter_s = Counter(new_s)
    values = counter_s.values()

    odd_count = 0
    for val in values:
        if val % 2 != 0:
            odd_count += 1
        
        if odd_count >= 2:
            return False
    return True


print(sol_1("Tact Coa"))
    