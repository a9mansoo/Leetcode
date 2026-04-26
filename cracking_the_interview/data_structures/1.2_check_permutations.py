from collections import Counter


def sol_1(s, t):
    list_s = list(s)
    list_s.sort()
    list_t = list(t)
    list_t.sort()
    return list_s == list_t


def sol_2(s, t):
    counter_s = Counter(s)
    counter_t = Counter(t)
    return counter_s == counter_t


sols = [sol_1, sol_2]


for sol in sols:
    print(sol("abc", "c"))
    print(sol("cba", "abc"))
    print(sol("b", "a"))