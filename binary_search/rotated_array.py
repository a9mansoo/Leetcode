nums = [4,5,6,7,0,1,2]
target = 0

def sol_1(nums, target):
    lo = 0
    high = len(nums) - 1

    while lo <= high:
        mid = (lo + high) // 2
        if nums[mid] == target:
            return mid
        
        # If mid > lo, then that side is
        # still sorted
        if nums[mid] >= nums[lo]:

            if target < nums[mid] and target >= nums[lo]:
                high = mid - 1
            else:
                lo = mid + 1
        
        else:
            # RHS is still sorted

            if target > nums[mid] and target <= nums[high]:
                lo = mid + 1
            else:
                high = mid - 1


print(sol_1(nums, target))