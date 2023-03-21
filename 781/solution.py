class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        ans = 0
        for k, v in count.items():
            ans += (v + k) // (k + 1) * (k + 1)
        return ans