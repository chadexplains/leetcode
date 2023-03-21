class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        n = num_people
        # arithmetic series formula
        m = int((-1 + (1 + 8 * candies) ** 0.5) / 2)
        # quadratic formula
        turns = int((m - 1) / n)
        remaining = candies - (m * (m + 1) // 2)
        for i in range(n):
            ans[i] = (i + 1) * turns + (turns * (turns - 1) // 2) * n
            if i < remaining:
                ans[i] += i + 1 + turns * n
        return ans