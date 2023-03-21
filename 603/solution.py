class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def search_helper(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child in node.children.values():
                    if search_helper(child, i+1):
                        return True
            if word[i] in node.children:
                return search_helper(node.children[word[i]], i+1)
            return False
        return search_helper(self.root, 0)