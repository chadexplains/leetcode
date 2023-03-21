def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        def dfs(pos):
            if pos == len(res):
                return True
            if res[pos]:
                return dfs(pos + 1)
            for i in range(n, 0, -1):
                if used[i]:
                    continue
                if i == 1:
                    res[pos] = 1
                    used[i] = True
                    if dfs(pos + 1):
                        return True
                    used[i] = False
                    res[pos] = 0
                elif pos + i < len(res) and not res[pos + i]:
                    res[pos], res[pos + i] = i, i
                    used[i] = True
                    if dfs(pos + 1):
                        return True
                    used[i] = False
                    res[pos], res[pos + i] = 0, 0
            return False
        dfs(0)
        return res