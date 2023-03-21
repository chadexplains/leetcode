class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        for i, j in stones:
            if i not in parent:
                parent[i] = i
            if j not in parent:
                parent[j] = j
            parent[find(i)] = find(j)
        return len(stones) - len({find(x) for x in parent})