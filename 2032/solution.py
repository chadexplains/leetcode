def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    unique = set()
    count = {}
    for num in nums1 + nums2 + nums3:
        if num in unique:
            count[num] += 1
        else:
            unique.add(num)
            count[num] = 1
    result = []
    for key, value in count.items():
        if value >= 2:
            result.append(key)
    return result