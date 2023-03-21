class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        children = defaultdict(list)
        for i in range(1, n):
            children[parents[i]].append(i)
        values = set(nums)
        result = [-1] * n
        def dfs(node):
            if nums[node] in values:
                values.remove(nums[node])
            for child in children[node]:
                dfs(child)
            smallest = float('inf')
            for i in range(1, 100002):
                if i not in values:
                    smallest = i
                    break
            result[node] = smallest
            values.add(smallest)
        dfs(0)
        return result