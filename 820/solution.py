class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        nodes = []
        for word in words:
            nodes.append(trie.insert(word[::-1]))
        return sum(len(word) + 1 for i, word in enumerate(words) if nodes[i].is_leaf())