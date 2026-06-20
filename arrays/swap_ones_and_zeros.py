nums = [1, 0, 0, 0, 1]

swaps = 0
ones = 0

for curr in range(len(nums)):

    if nums[curr] == 1:
        ones += 1
    else:
        swaps += ones

zeros = 0
swaps_zero = 0
for curr in range(len(nums)):

    if nums[curr] == 0:
        zeros += 1
    else:
        swaps_zero += zeros


print(min(swaps, swaps_zero))
