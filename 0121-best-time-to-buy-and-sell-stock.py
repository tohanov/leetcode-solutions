class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]

            profit = max(profit, price - buy_price)
            buy_price = min(buy_price, price)

        return profit


# Time complexity: O(|prices|)
# Space complexity: O(1)
