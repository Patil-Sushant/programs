# class Solution:
#     def profit(self, prices: list[int]) -> int:
#         i = 0
#         low = prices[0]
#         high = prices[0]
#         maxProfit = 0
#         n = len(prices)
    
#         while i < n-1:
#             while i < n-1 and prices[i] >= prices[i+1]:
#                 i += 1
#             low = prices[i]

#             while i < n-1 and prices[i] <= prices[i+1]:
#                 i += 1
#             high = prices[i]

#             maxProfit += high - low
#         return maxProfit

# stocks = Solution()
# stocks.profit([7, 1, 5, 3, 6, 4])

def profit(prices):
    i = 0
    low = prices[0]
    high = prices[0]
    maxProfit = 0
    n = len(prices)

    while i < n-1:
        while i < n-1 and prices[i] >= prices[i+1]:
            i += 1
        low = prices[i]

        while i < n-1 and prices[i] <= prices[i+1]:
            i += 1
        high = prices[i]

        maxProfit = maxProfit + high - low
    return maxProfit

print(profit([7, 1, 5, 3, 6, 4]))

# References
# https://www.youtube.com/watch?v=TSpBHe5vInA&pp=ygUdYnV5IGFuZCBzZWxsIHN0b2NrIGdyZWdnIGhvZ2c%3D

