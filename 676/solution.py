class MagicDictionary:
    
    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

    def search(self, searchWord: str) -> bool:
        def dfs(node, i, diff_count):
            if diff_count > 1:
                return False
            if i == len(searchWord):
                return '$' in node and diff_count == 1
            char = searchWord[i]
            for next_char in set(node.keys()) - {'$'}:
                if dfs(node[next_char], i+1, diff_count + (char != next_char)):
                    return True
            return False
        return dfs(self.trie, 0, 0)