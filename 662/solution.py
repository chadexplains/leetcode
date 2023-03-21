```python
from collections import deque
def widthOfBinaryTree(root):
    if not root:
        return 0
    queue = deque([(root, 0)])
    level_index = {}
    max_width = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node, index = queue.popleft()
            if i == 0 and index not in level_index:
                level_index[index] = index
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
            if i == level_size - 1:
                max_width = max(max_width, index - level_index[index] + 1)
    return max_width
```