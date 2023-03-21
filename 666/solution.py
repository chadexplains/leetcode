def pathSum(self, nums: List[int]) -> int:
    tree = {}
    for num in nums:
        depth, pos, val = num // 100, num % 100 // 10, num % 10
        tree[2 ** (depth - 1) + pos - 1] = val
    def dfs(node, running_sum):
        if node not in tree:
            return 0
        running_sum += tree[node]
        left, right = 2 * node + 1, 2 * node + 2
        if left not in tree and right not in tree:
            return running_sum
        return dfs(left, running_sum) + dfs(right, running_sum)
    return dfs(0, 0)