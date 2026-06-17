import heapq

nums = [1,1,1,2,2,3]
k = 2

freq_arr = []
seen = set()
for i in range(len(nums)):
    if nums[i] in seen:
        continue
    seen.add(nums[i])
    count = 1
    for j in range(i+1, len(nums)):
        if nums[j] == nums[i]:
            count += 1
    freq_arr.append((-count, nums[i]))

print(freq_arr)

heapq.heapify(freq_arr)
elems = []
for _ in range(k):
    elems.append(heapq.heappop(freq_arr)[1])
print(elems)