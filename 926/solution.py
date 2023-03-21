class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        num_flips_ending_0 = num_flips_ending_1 = 0
        for c in S:
            if c == '0':
                num_flips_ending_1 = min(num_flips_ending_0, num_flips_ending_1) + 1
            else:
                num_flips_ending_1 = min(num_flips_ending_0, num_flips_ending_1)
                num_flips_ending_0 += 1
        return min(num_flips_ending_0, num_flips_ending_1)