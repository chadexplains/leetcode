class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s.count('0')
        ones = 0
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros -= 1
            else:
                ones += 1
            score = zeros + ones
            if score > max_score:
                max_score = score
        return max_score