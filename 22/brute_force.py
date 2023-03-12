```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(combination, n):
            if len(combination) == 2 * n:
                if valid(combination):
                    ans.append(combination)
            else:
                combination += '('
                generate(combination, n)
                combination = combination[:-1]

                combination += ')'
                generate(combination, n)
                combination = combination[:-1]

        def valid(combination):
            bal = 0
            for c in combination:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate('', n)
        return ans
```