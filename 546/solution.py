class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        def calculatePoints(l, r, k):
            if l > r:
                return 0
            if dp[l][r][k] != 0:
                return dp[l][r][k]
            while r > l and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            dp[l][r][k] = calculatePoints(l, r-1, 0) + (k+1) * (k+1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], calculatePoints(l, i, k+1) + calculatePoints(i+1, r-1, 0))
            return dp[l][r][k]
        
        return calculatePoints(0, n-1, 0)