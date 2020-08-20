class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #          5
        #         / \
        #        /   \                     4
        # 3-----3     \             3     /
        #              \           / \   /
        #               \         /   \ /
        #                \       /     1
        #                 0-----0
                
        if not prices:
            return 0
        left, right = [0]*len(prices), [0]*len(prices)
        lMin, rMax = prices[0], prices[-1]
        for i in range(1, len(prices)):
            lMin = min(lMin, prices[i])
            left[i] = max(left[i-1], prices[i]-lMin)
        for i in range(len(prices)-2, -1, -1):
            rMax = max(rMax, prices[i])
            right[i] = max(right[i+1], rMax-prices[i])
        #print(left, right)
        ans = 0
        for i in range(len(left)-1):
            ans = max(ans, left[i] + right[i+1])
        return max(ans, right[0])