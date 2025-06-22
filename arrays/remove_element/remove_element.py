from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums[i] = "_"
            # now swap
            j = i + 1
            k = i
            while j < len(nums):
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                j += 1
                k += 1
            print(nums)
            i = 0
        elif val not in nums:
            break
        else:
            i += 1
        
    int_index = nums.index("_")
    nums = nums[:int_index]
    print(nums)
    return len(nums)
    
    






nums = [0,1,2,2,3,0,4,2]
val = 2

removeElement(nums, val)

nums = [3,2,2,3]
val = 3
removeElement(nums, val)