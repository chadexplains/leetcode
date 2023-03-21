class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.stream = deque()
        for word in words:
            node = self.trie
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for char in self.stream:
            if char in node.children:
                node = node.children[char]
                if node.is_word:
                    return True
            else:
                break
        return False