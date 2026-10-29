class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1 #out
        left = 0 #in
        ans = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if prices[right] < prices[left]:
                left = right
            else:            
                ans = max(ans, profit)
            right += 1
        return ans



