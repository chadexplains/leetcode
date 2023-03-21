class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        passwords = [str(i) for i in range(k**(n-1))]
        graph = {p: [] for p in passwords}
        for p in passwords:
            for d in range(k):
                graph[p].append(str(d) + p[:-1])
        path = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            path.append(node)
        dfs(passwords[0])
        return ''.join(path[::-1])