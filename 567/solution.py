class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        left, count = 0, len(freq)
        for right in range(len(s2)):
            if s2[right] in freq:
                freq[s2[right]] -= 1
                if freq[s2[right]] == 0:
                    count -= 1
            if right - left + 1 == len(s1):
                if count == 0:
                    return True
                if s2[left] in freq:
                    freq[s2[left]] += 1
                    if freq[s2[left]] == 1:
                        count += 1
                left += 1
        return False