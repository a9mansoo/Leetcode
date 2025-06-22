def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        
        curr_nums_1_elems = m
        num1_index = -1
        for num2 in nums2:
            while num1_index < len(nums1):
                num1_index += 1
                num1 = nums1[num1_index]
                if num1 > num2:
                    # shift elements
                    i = len(nums1) - 2
                    while i >= num1_index:
                        nums1[i+1] = nums1[i]
                        i = i - 1
                    nums1[i+1] = num2
                    curr_nums_1_elems += 1
                    break
                elif num1_index >= curr_nums_1_elems:
                     nums1[num1_index] = num2
                     curr_nums_1_elems += 1
                     break


nums1 = [1, 2, 3, 0 ,0, 0]
m = len(nums1)
nums2 = [2, 5, 6]
n = len(nums2)
m = len(nums1) - n

merge(nums1, m, nums2, n)
print(nums1)
nums1 = [-1,0,0,3,3,3,0,0,0]
m = len(nums1)
nums2 = [1,2,2]
n = len(nums2)
m = len(nums1) - n
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0,0,3,0,0,0,0,0,0]
m = len(nums1)
nums2 = [-1,1,1,1,2,3]
n = len(nums2)
m = len(nums1) - n
merge(nums1, m, nums2, n)
print(nums1)