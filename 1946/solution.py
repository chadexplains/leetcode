class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_list = list(map(int, num))
        changed = False
        for i in range(len(num_list)):
            if change[num_list[i]] > num_list[i]:
                num_list[i] = change[num_list[i]]
                changed = True
            elif change[num_list[i]] == num_list[i]:
                continue
            elif changed:
                break
        return ''.join(map(str, num_list))