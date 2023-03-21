class Solution:
    def uniqueLetterString(self, S: str) -> int:
        last = [-1] * 26
        prevLast = [-1] * 26
        ans = 0
        for i, c in enumerate(S):
            index = ord(c) - ord('A')
            ans += (i - last[index]) * (last[index] - prevLast[index])
            prevLast[index] = last[index]
            last[index] = i
        for index in range(26):
            ans += (len(S) - last[index]) * (last[index] - prevLast[index])
        return ans