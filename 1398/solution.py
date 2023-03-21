class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    left[j] += 1
                else:
                    right[j] += 1
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    ans += left[j]
                else:
                    ans += right[j]
        return ans