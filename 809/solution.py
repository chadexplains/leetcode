class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def get_groups(s):
            groups = []
            for i in range(len(s)):
                if i == 0 or s[i] != s[i-1]:
                    groups.append([s[i], 1])
                else:
                    groups[-1][1] += 1
            return groups
        S_groups = get_groups(S)
        count = 0
        for word in words:
            word_groups = get_groups(word)
            if len(S_groups) != len(word_groups):
                continue
            match = True
            for i in range(len(S_groups)):
                if S_groups[i][0] != word_groups[i][0] or (S_groups[i][1] < 3 and S_groups[i][1] != word_groups[i][1]) or S_groups[i][1] < word_groups[i][1]:
                    match = False
                    break
            if match:
                count += 1
        return count