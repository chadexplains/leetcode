class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                graph[leftChild[i]].append(i)
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                graph[rightChild[i]].append(i)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            return True
        root = leftChild[0] if leftChild[0] != -1 else rightChild[0]
        return dfs(root) and len(visited) == n