class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def search(m):
            p = pow(26, m) % q
            cur = reduce(lambda x, y: (x * 26 + y) % q, nums[:m], 0)
            seen = {cur}
            for i in range(m, n):
                cur = (cur * 26 + nums[i] - nums[i-m] * p) % q
                if cur in seen:
                    return i - m + 1
                seen.add(cur)
            return -1
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        q = 2**63 - 1
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if search(mid) != -1:
                left = mid + 1
            else:
                right = mid - 1
        start = search(left - 1)
        return S[start: start + left - 1]