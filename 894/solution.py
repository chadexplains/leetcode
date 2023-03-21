def allPossibleFBT(n):
    memo = {}
    def generate(n):
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, n-1, 2):
            left = generate(i)
            right = generate(n-i-1)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        memo[n] = res
        return res
    return generate(n)