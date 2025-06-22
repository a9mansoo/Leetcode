from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    lst_answers = []
    i = 0

    while i < len(nums):
        left = i + 1
        right = len(nums) - 1
        # If the previous numbers are the same
        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
            continue
        while left < right:
            sum_num = nums[left] + nums[i] + nums[right]
            if sum_num == 0:
                lst_answers.append([nums[left], nums[i], nums[right]])
                left += 1
                right -= 1
                # Continue if the previous number was the same as the
                # next one, since the list is sorted, we will avoid
                # the same summations again
                while left < right and nums[left] == nums[left - 1]:
                    print(nums[left])
                    left += 1
            elif sum_num < 0:
                left += 1
            elif sum_num > 0:
                right -= 1
        i += 1
    return lst_answers


nums = [-1,0,1,2,-1,-4]
threeSum(nums)

        