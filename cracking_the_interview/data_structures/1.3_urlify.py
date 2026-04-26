

def sol_1(s, length):
    s = s.rstrip()
    replaced = s.replace(" ", "%20")
    return replaced


def sol_2(s, length):
    i = 0
    new_s = ""
    while i < length:
        char = s[i]
        if char == " ":
            new_s += "%20"
        else:
            new_s += char
        i += 1
    return new_s

sols = [sol_1, sol_2]

for sol in sols:
    print(sol("Mr John Smith   ", 13))