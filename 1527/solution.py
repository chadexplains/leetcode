class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set()
        left_count, right_count = [], []
        for c in s:
            right.add(c)
            right_count.append(len(right))
        for c in s:
            left.add(c)
            left_count.append(len(left))
        count = 0
        for i in range(len(s) - 1):
            if left_count[i] == right_count[len(s) - 2 - i]:
                count += 1
        return count