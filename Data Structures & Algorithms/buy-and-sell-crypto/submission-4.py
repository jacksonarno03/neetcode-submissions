class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i

            else:
                current_profit = prices[i] - prices[min_index]

                if current_profit > profit:
                    profit = current_profit

        return profit