

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    start_window = 0
    i = 0
    curr_substring = ""
    curr_max = 0
    while i < n:
        curr_char = s[i]
        while curr_char in curr_substring:
            start_window += 1
            curr_substring = s[start_window:i]
        curr_substring += curr_char
        i += 1
        curr_max = max(curr_max, i - start_window)
    return curr_max


s = "abcabcbb"
lengthOfLongestSubstring(s)

s = "bbbbb"
lengthOfLongestSubstring(s)

s = "pwwkew"
lengthOfLongestSubstring(s)