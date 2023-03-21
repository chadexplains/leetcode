class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num, path):
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            if not num and len(path) >= 3:
                return True
            for i in range(len(num)):
                if num[0] == '0' and i > 0:
                    break
                cur = int(num[:i+1])
                if dfs(num[i+1:], path + [cur]):
                    return True
            return False
        return dfs(num, [])