class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def dfs(left, right, path):
            if len(path) >= len(right):
                if len(path) != len(right) or int(path) > int(right):
                    return
                if len(path) == len(left) and int(path) >= int(left):
                    self.count += 1
                return
            for key, val in self.mapping.items():
                if len(path) == 0 and key == '0' and len(right) != 1:
                    continue
                dfs(left, right, key + path + val)
        self.mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        self.count = 0
        dfs(low, high, '')
        dfs(low, high, '0')
        dfs(low, high, '1')
        dfs(low, high, '8')
        return self.count