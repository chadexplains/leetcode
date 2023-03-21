class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        s = list(s)
        p = list(p)
        left, right = 0, len(removable)
        while left <= right:
            mid = (left + right) // 2
            for i in range(mid):
                s[removable[i]] = ''
            j = 0
            for i in range(len(s)):
                if j < len(p) and s[i] == p[j]:
                    j += 1
            for i in range(mid):
                s[removable[i]] = s[removable[i] - i]
            if j == len(p):
                left = mid + 1
            else:
                right = mid - 1
        return right