class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        freq = collections.Counter(arr)
        res = 0
        for i in freq:
            for j in freq:
                k = target - i - j
                if i <= j <= k:
                    if i < j < k:
                        res += freq[i] * freq[j] * freq[k]
                    elif i == j < k:
                        res += freq[i] * (freq[i] - 1) // 2 * freq[k]
                    elif i < j == k:
                        res += freq[i] * freq[j] * (freq[j] - 1) // 2
        return res % MOD