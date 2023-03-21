def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    post_dict = {val: i for i, val in enumerate(post)}
    def buildTree(pre_start, pre_end, post_start, post_end):
        if pre_start > pre_end:
            return None
        root = TreeNode(pre[pre_start])
        if pre_start == pre_end:
            return root
        left_root_val = pre[pre_start + 1]
        left_root_index = post_dict[left_root_val]
        left_tree_size = left_root_index - post_start + 1
        root.left = buildTree(pre_start + 1, pre_start + left_tree_size, post_start, left_root_index)
        root.right = buildTree(pre_start + left_tree_size + 1, pre_end, left_root_index + 1, post_end - 1)
        return root
    return buildTree(0, len(pre) - 1, 0, len(post) - 1)