class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for eq in equations:
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                if x not in parent:
                    parent[x] = x
                if y not in parent:
                    parent[y] = y
                union(x, y)
        for eq in equations:
            if eq[1] == '!=':
                x, y = eq[0], eq[3]
                if x == y:
                    return False
                if x not in parent:
                    parent[x] = x
                if y not in parent:
                    parent[y] = y
                if find(x) == find(y):
                    return False
        return True