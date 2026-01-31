from collections import Counter

S = "abaaba"


def func(S):
    s = 0

    dct_subs = {}

    while s < len(S):
        end = s + 1
        while end < len(S) + 1:
            curr_sub = S[s:end]
            if curr_sub in dct_subs:
                dct_subs[curr_sub][1] += 1
            else:
                dct_subs[curr_sub] = [s, 1]
            end += 1
        s += 1

    print(dct_subs)

    curr_index = 100000
    min_len = 1000000
    uniq_elem = ""

    for key, items in dct_subs.items():
        if items[1] > 1:
            continue
        if len(key) == min_len:
            if items[0] < curr_index:
                min_len = len(key)
                curr_index = items[0]
                uniq_elem = key
        elif len(key) < min_len:
            min_len = len(key)
            curr_index = items[0]
            uniq_elem = key


    print(uniq_elem)
    return uniq_elem

print(func("aaa"))
print(func("abc"))
print(func("abcdabcde"))

