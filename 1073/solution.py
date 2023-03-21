class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = sum([(-2)**i * x for i, x in enumerate(arr1[::-1])])
        num2 = sum([(-2)**i * x for i, x in enumerate(arr2[::-1])])
        res = num1 + num2
        if res == 0:
            return [0]
        ans = []
        while res != 0:
            res, rem = divmod(res, -2)
            if rem < 0:
                res, rem = res + 1, rem + 2
            ans.append(rem)
        return ans[::-1]