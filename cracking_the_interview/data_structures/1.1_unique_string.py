from collections import Counter


def sol_1(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


def sol_2(s):
    counter = Counter(s)
    values = counter.values()
    for val in values:
        if val >= 2:
            return False
    return True


def sol_3(s):
    if len(s) <= 1:
        return True
    
    i = 0
    while i < len(s) - 1:
        next = i + 1
        while next < len(s):
            if s[i] == s[next]:
                return False
            next += 1
        i += 1
    return True


sols = [sol_1, sol_2, sol_3]


for sol in sols:
    print(sol("abc"))
    print(sol("aba"))
    print(sol("abcbc"))


    