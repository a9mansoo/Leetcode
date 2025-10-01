from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t):
            s_char = s[s_pointer]
            t_char = t[t_pointer]
            if t_char == s_char:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
            
            if s_pointer >= len(s):
                return True
        return False


def isSubsequence(s, t):
    # preprocess t into a hashmap
    char_dict = defaultdict(list)
    for index in range(len(t)):
        char_dict[t[index]].append(index)
    prev_index = -1

    for char in s:
        if char in char_dict:
            first_char_index = 0
            len_of_arr = len(char_dict[char])
            while first_char_index < len_of_arr:
                if char_dict[char][first_char_index] > prev_index:
                    prev_index = char_dict[char][first_char_index]
                    break
                first_char_index += 1
            else:
                return False
        else:
            return False
    return True





sol = Solution()

print(sol.isSubsequence(s = "abc", t = "ahbgdc"))

isSubsequence(s = "abc", t = "ahbgdc")
isSubsequence(s="aabc", t="abcabc")