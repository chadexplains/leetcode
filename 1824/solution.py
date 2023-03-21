def getMaximums(nums: List[int], requests: List[List[int]]) -> List[int]:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    def build_tree(node, start, end):
        if start == end:
            tree[node] = prefix_sum[start]
        else:
            mid = (start + end) // 2
            build_tree(2 * node, start, mid)
            build_tree(2 * node + 1, mid + 1, end)
            tree[node] = max(tree[2 * node], prefix_sum[mid + 1] - prefix_sum[start], prefix_sum[end + 1] - prefix_sum[mid + 1], tree[2 * node + 1])
    def query(node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return tree[node]
        mid = (start + end) // 2
        return max(query(2 * node, start, mid, left, right), query(2 * node + 1, mid + 1, end, left, right), prefix_sum[min(right, end) + 1] - prefix_sum[max(left, start)])
    tree = [0] * (4 * n)
    build_tree(1, 1, n)
    ans = []
    for left, right in requests:
        ans.append(query(1, 1, n, left + 1, right + 1))
    return ans