class Solution(object):
    def maxProfit(self, prices):
        maxi = mini = profit = 0
        for i in range (len(prices)):
            if i == 0:
                maxi = mini = prices [i]
            elif mini>prices[i]:
                mini = maxi = prices[i]
            elif maxi< prices[i]:
                maxi = prices [i]
                if maxi - mini > profit:
                    profit = maxi - mini
        return profit
