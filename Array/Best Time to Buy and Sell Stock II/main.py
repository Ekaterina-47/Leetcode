# function:
def maxProfit(prices):
    pos = 0
    max_profit = 0
    for i in range(0, len(prices) - 1):
        if i < pos:
            continue
        if i == 0 and prices[i] < prices[i + 1]:
            max_profit -= prices[i]
        elif prices[i] <= prices[i - 1] and prices[i] < prices[i + 1]:
            max_profit -= prices[i]
        else:
            pos += 1
            continue
        for j in range(i + 1, len(prices)):
            pos = j
            if j != len(prices) - 1:
                if prices[j] >= prices[j - 1] and prices[j] > prices[j + 1]:
                    max_profit += prices[j]
                    break
            elif prices[j] >= prices[j - 1]:
                max_profit += prices[j]
                break
    return max_profit

# tests:
print(maxProfit([7, 5, 3, 1, 0, 2, 9, 2, 1, 9, 9, 2]))
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 2, 5]))
