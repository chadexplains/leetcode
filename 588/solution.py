class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''
        self.is_file = False


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.root
        files = []
        if path != '/':
            dirs = path.split('/')
            for d in dirs[1:]:
                node = node.children[d]
        if node.is_file:
            return [dirs[-1]]
        for n in node.children:
            if node.children[n].is_file:
                files.append(n)
            else:
                files.append(n + '/')
        return sorted(files)

    def mkdir(self, path: str) -> None:
        node = self.root
        dirs = path.split('/')
        for d in dirs[1:]:
            if d not in node.children:
                node.children[d] = TrieNode()
            node = node.children[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        dirs = filePath.split('/')
        for d in dirs[1:-1]:
            node = node.children[d]
        if dirs[-1] not in node.children:
            node.children[dirs[-1]] = TrieNode()
            node.children[dirs[-1]].is_file = True
        node = node.children[dirs[-1]]
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        dirs = filePath.split('/')
        for d in dirs[1:]:
            node = node.children[d]
        return node.content
