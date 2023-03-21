```def findStrobogrammatic(n: int) -> List[str]:
    pairs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
    res = []
    def dfs(s, left, right):
        if left > right:
            res.append(s)
            return
        if left == right:
            for c in ["0", "1", "8"]:
                dfs(s+c, left+1, right-1)
            return
        for k, v in pairs.items():
            if left == 0 and k == "0":
                continue
            dfs(k+s+v, left+1, right-1)
    dfs("", 0, n-1)
    return res```