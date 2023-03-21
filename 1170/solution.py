class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        freq = sorted([f(w) for w in words])
        res = []
        for q in queries:
            qf = f(q)
            l, r = 0, len(words) - 1
            while l <= r:
                mid = (l + r) // 2
                if freq[mid] <= qf:
                    l = mid + 1
                else:
                    r = mid - 1
            res.append(len(words) - l)
        return res
