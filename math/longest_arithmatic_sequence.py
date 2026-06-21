arr = [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9]
k = 2

s = set(arr)
s = list(s)
max_len = 0

for x in s:

    if (x-k) in s:
        continue

    curr_elem = 1
    curr = x
    while curr+k in s:
        curr_elem += 1
        curr += k
    
    max_len = max(max_len, curr_elem)

print(max_len)
