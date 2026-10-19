from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if "a" not in s and "e" not in s and "i" not in s and "o" not in s and "u" not in s:
            return 0
        
        vowels = set(["a", "e", "i", "o", "u"])
        max_vowels = float('-Inf')

        start = 0
        end = 0
        total_vowels = 0

        while end < len(s):
            char = s[end]
            if char in vowels:
                total_vowels += 1

            
            while (end - start + 1) > k:
                last_char = s[start]
                if last_char in vowels:
                    total_vowels -= 1
                start += 1
            
            max_vowels = max(max_vowels, total_vowels)
            end += 1
        return max_vowels
