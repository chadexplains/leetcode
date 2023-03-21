def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    left, right = 0, len(properties) - 1
    count = 0
    while left < right:
        if properties[left][1] < properties[right][1]:
            count += 1
            left += 1
        else:
            right -= 1
    return count