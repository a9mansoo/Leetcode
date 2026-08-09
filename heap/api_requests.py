import heapq


requests = [
    ("a", 1),
    ("b", 2),
    ("a", 3),
    ("c", 4),
    ("a", 5),
    ("b", 6)
]

k = 2

heap = []

heapq.heapify(heap)


for request in requests:

    if heap and heap[0][0] < request[1]:
        heapq.heappush(heap, (request[1], request[0]))
        while len(heap) > k:
            heapq.heappop(heap)

    if not heap:
        heapq.heappush(heap, (request[1], request[0]))

res = []
for i in range(0, k):
    user = heapq.heappop(heap)
    res.append(user[1])

print(res)