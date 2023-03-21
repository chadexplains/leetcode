class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    right[i] += 1
                elif rating[j] < rating[i]:
                    left[i] += 1
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    ans += right[j]
                elif rating[j] < rating[i]:
                    ans += left[j]
        return ans