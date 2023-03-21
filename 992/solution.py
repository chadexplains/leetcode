class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMostK(k):
            count = collections.Counter()
            res = i = 0
            for j in range(len(A)):
                if count[A[j]] == 0: k -= 1
                count[A[j]] += 1
                while k < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0: k += 1
                    i += 1
                res += j - i + 1
            return res
        return atMostK(K) - atMostK(K - 1)