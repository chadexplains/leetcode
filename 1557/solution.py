class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        for edge in edges:
            incoming.add(edge[1])
        return list(set(range(n)) - incoming)