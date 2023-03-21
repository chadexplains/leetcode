class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set()
        left_count, right_count = [], []
        for c in s:
            right.add(c)
            right_count.append(len(right))
        for c in s[::-1]:
            left.add(c)
            left_count.append(len(left))
        left_count.reverse()
        count = 0
        for i in range(1, len(s)):
            if left_count[i-1] == right_count[i]:
                count += 1
        return count