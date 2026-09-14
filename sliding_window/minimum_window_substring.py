class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dct_t_counter = {}
        dct_orig_counter = {}

        for char in t:
            dct_orig_counter[char] = dct_orig_counter.get(char, 0) + 1

        start = 0
        end = 0

        min_start = 0
        minimum_len = float('inf')

        required = len(dct_orig_counter)
        formed = 0

        while end < len(s):
            char = s[end]

            if char in dct_orig_counter:
                dct_t_counter[char] = dct_t_counter.get(char, 0) + 1

                if dct_t_counter[char] == dct_orig_counter[char]:
                    formed += 1

            while formed == required:

                if end - start + 1 < minimum_len:
                    min_start = start
                    minimum_len = end - start + 1

                start_char = s[start]

                if start_char in dct_t_counter:
                    dct_t_counter[start_char] -= 1

                    if dct_t_counter[start_char] < dct_orig_counter[start_char]:
                        formed -= 1

                start += 1

            end += 1

        if minimum_len == float('inf'):
            return ""

        return s[min_start:min_start + minimum_len]
