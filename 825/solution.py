class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1
        total_requests = 0
        for age_a in range(1, 121):
            count_a = age_count[age_a]
            for age_b in range(int(0.5 * age_a + 8), age_a):
                count_b = age_count[age_b]
                total_requests += count_a * count_b
                if age_a == age_b:
                    total_requests -= count_a
        return total_requests