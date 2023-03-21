class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(heap) < k:
                    heappush(heap, [nums1[i] + nums2[j], i, j])
                elif nums1[i] + nums2[j] < heap[0][0]:
                    heappop(heap)
                    heappush(heap, [nums1[i] + nums2[j], i, j])
        return [[nums1[i], nums2[j]] for _, i, j in heap]