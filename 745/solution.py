class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_indices = []


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_trie = TrieNode()
        self.suffix_trie = TrieNode()
        for i, word in enumerate(words):
            self._insert_word(word, i)

    def f(self, prefix: str, suffix: str) -> int:
        prefix_words = self._get_words_with_prefix(prefix, self.prefix_trie)
        suffix_words = self._get_words_with_prefix(suffix[::-1], self.suffix_trie)
        i, j = len(prefix_words) - 1, len(suffix_words) - 1
        while i >= 0 and j >= 0:
            if prefix_words[i] == suffix_words[j]:
                return prefix_words[i]
            elif prefix_words[i] > suffix_words[j]:
                i -= 1
            else:
                j -= 1
        return -1

    def _insert_word(self, word: str, index: int) -> None:
        node = self.prefix_trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_indices.append(index)
        node = self.suffix_trie
        for char in word[::-1]:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_indices.append(index)

    def _get_words_with_prefix(self, prefix: str, trie: TrieNode) -> List[int]:
        node = trie
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.word_indices