class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, curr_sum, seen):
            if not node:
                return 0
            curr_sum += node.val
            complement = curr_sum - targetSum
            count = seen.get(complement, 0)
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
            res = count + helper(node.left, curr_sum, seen) + helper(node.right, curr_sum, seen)
            seen[curr_sum] -= 1
            if seen[curr_sum] == 0:
                del seen[curr_sum]
            return res
        return helper(root, 0, {0: 1})