

def gcd(num_1, num_2):

    while (num_1 != num_2):

        if (num_1 > num_2):
            num_1 = num_1 - num_2
        
        elif (num_2 > num_1):
            num_2 = num_2 - num_1
    
    return num_2


gcd(10, 5)
