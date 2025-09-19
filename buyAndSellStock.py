# def maxProfit(prices):
#     minPrice = prices[0]
#     maxProfit = 0
#     for price in prices[1:]:
#         # print(price)
#         maxProfit = max(maxProfit, price - minPrice)
#         minPrice = min(minPrice, price)
#     return maxProfit


# print(maxProfit([4, 2, 3, 9, 6]))

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/3914105/most-optimized-solution-easy-to-understand-c-java-python/
# another link
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1545423/python-easy-to-understand-solution-with-explanation-tracking-and-dynamic-programming/

def Profit(prices):
    maxProfit = 0
    minPrice = prices[0]
    for price in prices[1:]:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice = min(minPrice, price)
    return maxProfit

print(Profit([4, 2, 3, 9, 6]))