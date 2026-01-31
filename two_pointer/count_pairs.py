

def count_pairs(prices, budget):
    pairs = 0
    left = 0
    right = len(prices) - 1

    while left < right:
        if prices[left] + prices[right] <= budget:
            pairs += right - left
            left += 1
        else:
            right -= 1
    return pairs
