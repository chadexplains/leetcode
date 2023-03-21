class Solution:
    def countLetters(self, S: str) -> int:
        count = start = end = 0
        for i in range(len(S)):
            if S[i] != S[start]:
                count += (end - start) * (end - start + 1) // 2
                start = end
            end = i
        count += (end - start) * (end - start + 1) // 2
        return count