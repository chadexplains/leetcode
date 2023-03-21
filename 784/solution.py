class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def backtrack(i, curr):
            if i == len(S):
                res.append(curr)
                return
            if S[i].isalpha():
                backtrack(i+1, curr+S[i].lower())
                backtrack(i+1, curr+S[i].upper())
            else:
                backtrack(i+1, curr+S[i])
        backtrack(0, "")
        return res