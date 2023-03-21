class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        i, j, count = 0, 0, 0
        while count < n1:
            for k in range(len(s1)):
                if s1[k] == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1
            i += 1
            if i == len(s1):
                i = 0
        return count // n2 if count > 0 else -1