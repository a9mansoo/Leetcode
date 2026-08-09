


def longest_substring(s, k):
    start = 0
    end = 0
    max_len = float('-Inf')

    seen = {}

    while end < len(s):
        curr_char = s[end]
        seen[curr_char] = seen.get(curr_char, 0) + 1

        while start < len(s) and len(seen) > k:
            last_char = s[start]
            seen[last_char] -= 1
            start += 1

            if seen[last_char] == 0:
                del seen[last_char]

        max_len = max((end - start + 1), max_len)
        end += 1

    return max_len
