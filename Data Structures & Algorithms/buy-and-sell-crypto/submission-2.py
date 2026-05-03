class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp =0
        l,r =0, 1
        while r < len(prices):
            if prices[l]<prices[r]:
                p = prices[r] -prices[l]
                mp = max(mp,p)
                r=r+1
            else:
                l=r
                r=r+1
        return mp