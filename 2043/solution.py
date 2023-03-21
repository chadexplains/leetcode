class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n+1):
            s = sum(int(c) for c in str(i))
            d[s] = d.get(s, 0) + 1
        max_freq = max(d.values())
        return sum(1 for freq in d.values() if freq == max_freq)