class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1, p2, p3 = 0, 0, 0
        intersection = set()
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                intersection.add(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                min_val = min(arr1[p1], arr2[p2], arr3[p3])
                if arr1[p1] == min_val:
                    p1 += 1
                if arr2[p2] == min_val:
                    p2 += 1
                if arr3[p3] == min_val:
                    p3 += 1
        return list(intersection)