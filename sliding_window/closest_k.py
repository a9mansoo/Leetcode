arr = [1,2,3,4,5,6,7,8]
k = 3
x = 4

left = 0
right = len(arr) - 1

while left < right:
    a = arr[left]
    b = arr[right]

    if (right - left) + 1 == k:
        break
    
    if abs(a - x) < abs(b-x) or (abs(a-x) == abs(b-x) and a < b):
        right -= 1
    else:
        left += 1

print(arr[left:right+1])
