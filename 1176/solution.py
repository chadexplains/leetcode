class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int) -> int:
        score = 0
        window_sum = sum(calories[:k-1])
        for i in range(k-1, len(calories)):
            window_sum += calories[i]
            if window_sum < k:
                score += 1
            elif window_sum >= k:
                score -= 1
            window_sum -= calories[i-k+1]
        return score