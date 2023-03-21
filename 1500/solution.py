class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class FileSystem:
    def __init__(self):
        self.root = Node(None)

    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        components = path.split('/')[1:]
        for c in components[:-1]:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if components[-1] in cur.children:
            return False
        cur.children[components[-1]] = Node(value)
        return True

    def get(self, path: str) -> int:
        cur = self.root
        components = path.split('/')[1:]
        for c in components:
            if c not in cur.children:
                return -1
            cur = cur.children[c]
        return cur.val