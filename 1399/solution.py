class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n+1):
            s = sum(int(c) for c in str(i))
            d[s] = d.get(s, 0) + 1
        max_count = max(d.values())
        return sum(1 for count in d.values() if count == max_count)