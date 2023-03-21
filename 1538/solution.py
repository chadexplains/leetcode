class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > max_element:
                max_element = arr[i]
                count = 0
            count += 1
            if count == k:
                return max_element
            if count >= len(arr) - k:
                break
        return max_element