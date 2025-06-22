def isPalindrome(s):
    
    lst_filtered = list(filter(lambda x: x.isalnum(), s))
    lst_lowered = list(map(lambda x: x.lower(), lst_filtered))
    s = "".join(lst_lowered)
    int_end = len(s) - 1
    int_start = 0
    while int_start < int_end:
        curr_start = s[int_start]
        curr_end = s[int_end]

        while not curr_start.isalnum() and int_start < len(s) - 1:
            int_start += 1
            curr_start = s[int_start]
        while not curr_end.isalnum() and int_end > 0:
            int_end -= 1
            curr_end = s[int_end]
        
        if int_start > int_end:
            return False

        if curr_start.lower() == curr_end.lower():
            int_start += 1
            int_end -= 1
        else:
            return False
    return True




s = "race a car"


print(isPalindrome(s))

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))

s = "aa"
print(isPalindrome(s))

s = "a"
print(isPalindrome(s))

s = "0P"
print(isPalindrome(s))

s = " "
print(isPalindrome(s))

s = ".,"
print(isPalindrome(s))