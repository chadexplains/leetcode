class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2_set = set(arr2)
        distance = 0
        for num in arr1:
            for i in range(num-d, num+d+1):
                if i in arr2_set:
                    break
            else:
                distance += 1
        return distance