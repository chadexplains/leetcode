class TrieNode:
    def __init__(self):
        self.value = None
        self.children = {}


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        for p in path.split('/')[1:]:
            if p not in curr.children:
                curr.children[p] = TrieNode()
            curr = curr.children[p]
            if curr.value is not None:
                return False
        curr.value = value
        return True

    def get(self, path: str) -> int:
        curr = self.root
        for p in path.split('/')[1:]:
            if p not in curr.children:
                return -1
            curr = curr.children[p]
        return curr.value if curr.value is not None else -1