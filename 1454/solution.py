class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = {}
        t_freq = {}
        for c in s:
            s_freq[c] = s_freq.get(c, 0) + 1
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        steps = 0
        for k in s_freq.keys():
            steps += abs(s_freq[k] - t_freq.get(k, 0))
        return steps