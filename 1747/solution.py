class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change_dict = {str(i): str(change[i]) for i in range(10)}
        result = []
        for digit in num:
            if change_dict[digit] > digit:
                result.append(change_dict[digit])
                break
            result.append(digit)
        result.extend([change_dict[digit] for digit in num[len(result):]])
        return ''.join(result)