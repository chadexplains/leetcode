class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        freq = Counter(nums)
        dp = [0] * (1 << 10)
        dp[0] = 1
        for num, count in freq.items():
            if num == 1 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                continue
            mask = 0
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    if i == 2:
                        mask |= 1
                    elif i == 3:
                        mask |= 2
                    elif i == 5:
                        mask |= 4
                    elif i == 7:
                        mask |= 8
                    if num // i != i:
                        if num // i == 2:
                            mask |= 1
                        elif num // i == 3:
                            mask |= 2
                        elif num // i == 5:
                            mask |= 4
                        elif num // i == 7:
                            mask |= 8
            for i in range(len(dp) - 1, -1, -1):
                if dp[i] == 0:
                    continue
                new_mask = i | mask
                if new_mask & 1:
                    continue
                if bin(new_mask).count('1') > 1:
                    continue
                dp[new_mask] += dp[i] * pow(2, count - 1, MOD)
                dp[new_mask] %= MOD
        return sum(dp) % MOD