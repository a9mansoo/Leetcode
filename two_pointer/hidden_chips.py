


def hiddenChips(imageDim, k):
    imageDim.sort()
    int_curr = 0
    length_dim = len(imageDim)
    hidden = 0
    int_next = int_curr + 1

    while int_curr < length_dim:
        value = imageDim[int_curr] * k
        if int_next >= length_dim:
            break

        if value <= imageDim[int_next]:
            hidden += 1
            int_curr += 1
            int_next += 1
        else:
            int_next += 1
    
    return hidden

        
        



hiddenChips([6, 4, 2, 4, 8], 2)
hiddenChips([4, 2, 6, 14], 3)