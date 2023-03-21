class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = Counter(letters)
        scores = {chr(i + 97): score[i] for i in range(26)}
        def dfs(i):
            if i == len(words):
                return 0
            skip = dfs(i + 1)
            can_use = True
            cur_score = 0
            for c in words[i]:
                if freq[c] == 0:
                    can_use = False
                    break
                freq[c] -= 1
                cur_score += scores[c]
            if can_use:
                use = cur_score + dfs(i + 1)
            else:
                use = 0
            for c in words[i]:
                freq[c] += 1
            return max(skip, use)
        return dfs(0)