class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def dfs(x, left):
            count = 0
            if left == 0:
                return 1
            for y in graph[x]:
                if visited[y] or (y in graph[x] and freq[y] == freq[y-1] and not visited[y-1]):
                    continue
                visited[y] = True
                freq[y] -= 1
                count += dfs(y, left-1)
                freq[y] += 1
                visited[y] = False
            return count
        freq = collections.Counter(A)
        graph = {x: {y for y in freq if int((x+y)**0.5)**2 == x+y}}
        for x in freq:
            graph[x] |= {y for y in freq if int((x+y)**0.5)**2 == x+y}
        visited = {x: False for x in freq}
        return sum(dfs(x, len(A)-1) for x in freq)