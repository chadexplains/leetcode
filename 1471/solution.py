class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        left, right = 0, len(arr)-1
        res = []
        while len(res) < k:
            if abs(arr[left]-median) > abs(arr[right]-median):
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right -= 1
        return res