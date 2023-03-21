class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return ['']
            res = []
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet:
                    for sentence in backtrack(end):
                        res.append(s[start:end] + (' ' if sentence else '') + sentence)
            memo[start] = res
            return res
        return backtrack(0)