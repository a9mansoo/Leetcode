


def sliding_window(substring):
    start = 0
    end = 1
    curr = start
    max_len = -1

    while start < len(substring) - 1:
        curr = start + 1

        while curr < len(substring):
            curr_char = substring[curr]
            if curr_char not in substring[start:curr - 1]:
                max_len = len(substring[start:curr+1])
                curr += 1
            else:
                break
        start += 1
    return max_len



print(sliding_window("abcabcbb"))