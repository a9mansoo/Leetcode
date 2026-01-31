from collections import Counter

def isNonTrivialRotation(s1, s2):
    # Write your code here
    counter = Counter(s1)
    counter_2 = Counter(s2)
    
    if counter != counter_2:
        return 0
    
    if len(s1) == 1:
        return False
    
    s2_1 = 0
    s1_1 = 0
    start_index = -1
    curr_s1 = 0
    while s1_1 < len(s1):
        if s1[s1_1] == s2[s2_1]:
            print(f"S1: {s1[s1_1]} S2: {s2[s2_1]}")
            start_index = s1_1
            curr_s1 = s1_1 + 1
            s2_1 += 1
            while s1[curr_s1] == s2[s2_1]:
                print(f"S1: {s1[curr_s1]} S2: {s2[s2_1]}")
                curr_s1 += 1
                if curr_s1 >= len(s1):
                    curr_s1 = 0
                s2_1 += 1
                if s2_1 >= len(s2):
                    s1_1 = len(s1)
                    break
        s1_1 += 1
        s2_1 = 0
    
    if start_index == -1 or start_index == 0:
        return False
    return True


print(isNonTrivialRotation("abcde", "cdeab"))
print(isNonTrivialRotation("abcde", "abcde"))
print(isNonTrivialRotation("abccde", "cdeabc"))