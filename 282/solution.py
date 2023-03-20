class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(expr, val, last):
            nonlocal ans
            if not num:
                if val == target:
                    ans.append(expr)
                return
            for i in range(1, len(num) + 1):
                if i != 1 and num[0] == '0':
                    break
                cur = int(num[:i])
                if not expr:
                    backtrack(num[i:], cur, cur)
                else:
                    backtrack(expr + '+' + num[:i], val + cur, cur)
                    backtrack(expr + '-' + num[:i], val - cur, -cur)
                    backtrack(expr + '*' + num[:i], val - last + last * cur, last * cur)
            return
        ans = []
        backtrack('', 0, 0)
        return ans