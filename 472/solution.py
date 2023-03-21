class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        output = []
        for word in words:
            if len(word) == 0:
                continue
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(len(word)):
                if not dp[i]:
                    continue
                for j in range(i + 1, len(word) + 1):
                    if j - i < len(word) and word[i:j] in word_set:
                        dp[j] = True
                if dp[-1]:
                    output.append(word)
                    break
        return output