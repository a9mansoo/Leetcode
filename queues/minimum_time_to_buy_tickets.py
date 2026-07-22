from collections import deque

tickets = [2,3,2]

k = 2

q = deque(list(range(len(tickets) - 1)))
time = 0

while q:
    time += 1
    curr = q.popleft()

    tickets[curr] = tickets[curr] - 1

    if k == curr and tickets[curr] == 0:
        break
    
    if tickets[curr] != 0:
        q.append(curr)

print(time)