class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ''


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
            node.word = word
        res = []
        for word in sentence.split():
            node = root
            for c in word:
                if c not in node.children or node.is_word:
                    break
                node = node.children[c]
            res.append(node.word if node.is_word else word)
        return ' '.join(res)