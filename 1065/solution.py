class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["end"] = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "end" in node


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        for i in range(len(text)):
            node = trie.root
            for j in range(i, len(text)):
                if text[j] not in node:
                    break
                node = node[text[j]]
                if "end" in node:
                    res.append([i, j])
        return res
