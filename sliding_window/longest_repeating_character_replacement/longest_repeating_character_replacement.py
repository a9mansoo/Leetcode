from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = left
        
        curr_max = -1
        chars = defaultdict(int)
        max_freq = -1

        while right < len(s):
            chars[s[right]] += 1
            max_freq = max(max_freq, chars[s[right]])

            while (right - left + 1) - max_freq > k:
                chars[s[left]] -= 1
                left += 1
            
            curr_max = max(curr_max, (right - left + 1))
            right += 1


        return curr_max


b = Solution()

#print(b.characterReplacement("ABAB", 2))
print(b.characterReplacement("AABABBA", 1))
print(b.characterReplacement("AAAA", 2))