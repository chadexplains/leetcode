def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    mapping = {piece[0]: piece for piece in pieces}
    i = 0
    while i < len(arr):
        if arr[i] not in mapping:
            return False
        piece = mapping[arr[i]]
        for num in piece:
            if num != arr[i]:
                return False
            i += 1
    return True