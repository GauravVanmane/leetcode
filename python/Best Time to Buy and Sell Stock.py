def maxProfit(self, prices: List[int]) -> int:
    min_number = float("inf")
    profit = 0
    for i in range(len(prices)):
        min_number = min(min_number, prices[i])
        profit = max(prices[i] - min_number, profit)
    return profit