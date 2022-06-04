# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


prices = [7,6,4,3,1,6]

# TLE ERROR!!! O(n^2)
# max_profit = 0
# for i in range(len(prices)-1):
#     buy = prices[i]
#     for j in range(i,len(prices)):
#         sell = prices[j]
#         profit = sell - buy
#         if profit>max_profit:
#             max_profit = profit

# print(max_profit) 

max_profit = 0
min_buy = float('inf')
for price in prices:
    min_buy=min(min_buy, price)
    max_profit=max(max_profit, price-min_buy)

print(max_profit)