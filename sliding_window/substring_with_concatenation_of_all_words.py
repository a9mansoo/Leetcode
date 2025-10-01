from typing import List
from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        char_len = len(words[0])
        substring_length = char_len * len(words)
        counter = Counter(words)
        len_str = len(s)

        start_window = 0
        window = start_window + substring_length
        lst_indices = []
        counter_map = defaultdict(int)
        # increment the start window till the point we 
        # have a long enough string
        while start_window <= len_str - substring_length:
            left = start_window
            right = left + char_len
            
            while right <= window:
                substr = s[left:right]
                if substr in words:
                    counter_map[substr] += 1
                if counter_map[substr] > counter[substr]:
                    break
                right += char_len
                left += char_len
            
            if counter == counter_map:
                lst_indices.append(start_window)
            
            start_window += 1
            window = start_window + substring_length
            
        return lst_indices



sol = Solution()

print(sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))