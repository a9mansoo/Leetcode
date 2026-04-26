


def sol_1(s):
    new_s = ""
    i = 0
    while i < len(s):
        curr_count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                curr_count += 1
            else:
                break
        new_s += s[i]
        new_s += str(curr_count)
        i += curr_count
    if len(new_s) > len(s):
        return s
    return new_s


print(sol_1("aabcccccaaa"))
