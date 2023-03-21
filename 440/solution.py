class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countNodes(prefix: int, n: int) -> int:
            count = 0
            next_prefix = prefix + 1
            while prefix <= n:
                count += min(n + 1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10
            return count
        curr = 1
        k -= 1
        while k > 0:
            count = countNodes(curr, n)
            if k >= count:
                curr += 1
                k -= count
            else:
                curr *= 10
                k -= 1
        return curr