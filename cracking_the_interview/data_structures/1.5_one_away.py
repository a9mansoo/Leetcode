


def one_away(s, t):
    edits = 0
    i, j = 0, 0
    shorter_string = s if len(s) < len(t) else t
    longer_string = t if len(s) < len(t) else s

    while i < len(shorter_string) and j < len(longer_string):
        if shorter_string[i] == longer_string[j]:
            i += 1
            j += 1
        else:
            if len(shorter_string) == len(longer_string):
                i += 1
                j += 1
            else:
                j += 1
            edits += 1
    if edits > 1:
        return False
    return True


print(one_away("pale", "ple"))
print(one_away("pale", "pales"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))