


def brackets(string):
    stack = []
    map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for char in string:
        if char in map:
            stack.append(char)
        elif stack and char == map[stack[-1]]:
            stack.pop()
        else:
            return False
    
    if stack:
        return False
    return True


#brackets("[([])]")
brackets("[([]]")