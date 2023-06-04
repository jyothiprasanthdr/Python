class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            elif prices[i] - buy_price > max_profit:
                max_profit = prices[i] - buy_price
        return max_profit
