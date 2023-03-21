class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(start, seq):
            if len(seq) >= 3 and seq[-1] != seq[-2] + seq[-3]:
                return
            if start == len(S):
                if len(seq) >= 3:
                    self.res = seq
                return
            for i in range(start, len(S)):
                if S[start] == '0' and i > start:
                    return
                num = int(S[start:i+1])
                if num > 2**31 - 1:
                    return
                if len(seq) < 2 or num == seq[-1] + seq[-2]:
                    backtrack(i+1, seq + [num])
                    if self.res:
                        return
        self.res = []
        backtrack(0, [])
        return self.res