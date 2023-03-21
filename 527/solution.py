class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def abbrev(word, i):
            if len(word) - i <= 3: return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]
        groups = collections.defaultdict(list)
        for i, word in enumerate(dict):
            groups[abbrev(word, 0)].append(i)
        ans = [None] * len(dict)
        for cand, indexes in groups.items():
            if len(indexes) == 1:
                ans[indexes[0]] = cand
            else:
                trie = {}
                for i in indexes:
                    node = trie
                    for letter in dict[i][1:]:
                        if letter not in node:
                            node[letter] = {}
                        node = node[letter]
                    node[None] = i
                for i in indexes:
                    node = trie
                    prefix = ''
                    for letter in dict[i][1:]:
                        node = node[letter]
                        prefix += letter
                        if len(node) == 1: break
                    ans[i] = dict[i][:len(prefix)+1] + str(len(dict[i])-len(prefix)-2) + dict[i][-1] if len(dict[i])-len(prefix) > 2 else dict[i]
        return ans