class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = [0] * 26
        t_freq = [0] * 26
        for c in s:
            s_freq[ord(c) - ord('a')] += 1
        for c in t:
            t_freq[ord(c) - ord('a')] += 1
        steps = 0
        for i in range(26):
            steps += abs(s_freq[i] - t_freq[i])
        return steps