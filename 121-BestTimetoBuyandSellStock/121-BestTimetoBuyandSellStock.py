class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force approach
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        # return max_profit

        # Time complexity = O(N) => N = number of days
        # Space Complexity = O(1)

        # Optimized approach
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

        # Time Complexity = O(N) => N = number of days
        # Space Complexity = O(1)