fruits = [1, 1, 2, 3, 1, 1, 2, 2]


start = 0
end = 0
max_len = -1
counts = {}
k = 2

while end < len(fruits):
    new_tree = fruits[end]

    counts[new_tree] = counts.get(new_tree, 0) + 1

    while len(counts) > k:
        old_tree = fruits[start]
        counts[old_tree] -= 1

        if counts[old_tree] == 0:
            del counts[old_tree]
        start += 1
    
    max_len = max(max_len, (end - start) + 1)
    end += 1

print(max_len)