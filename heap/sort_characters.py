

def sol(s):
    counter = {}

    for c in s:
        counter[c] = counter.get(c, 0) + 1
    
    max_val = max([i for _, i in counter.items()])

    buckets = [[] for _ in range(max_val, -1, -1)]

    for c in counter.keys():
        buckets[counter[c]].append(c)
    
    new_s = ""
    for bucket in range(len(buckets) - 1, -1, -1):
        if len(buckets[bucket]) <= 0:
            continue

        for c in buckets[bucket]:
            new_s += c * bucket
    
    print(new_s)

sol("tree")