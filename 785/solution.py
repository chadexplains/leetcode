class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if color[neighbor] == 0:
                            color[neighbor] = -color[node]
                            stack.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True