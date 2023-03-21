class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        count1 = count2 = 0
        for i in range(2 * n):
            if i % 2 == 0:
                count1 += s[i] != '0'
                count2 += s[i] != '1'
            else:
                count1 += s[i] != '1'
                count2 += s[i] != '0'
        return min(count1, count2)