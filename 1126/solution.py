```python

def maximumAverageSubtree(root):
    def dfs(node):
        nonlocal max_avg
        if not node:
            return 0, 0
        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)
        curr_sum = left_sum + right_sum + node.val
        curr_count = left_count + right_count + 1
        curr_avg = curr_sum / curr_count
        max_avg = max(max_avg, curr_avg)
        return curr_sum, curr_count
    max_avg = float('-inf')
    dfs(root)
    return max_avg
```