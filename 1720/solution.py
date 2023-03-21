def decode(encoded: List[int], first: int) -> List[int]:
    decoded = [first]
    for i in encoded:
        decoded.append(i ^ decoded[-1])
    return decoded