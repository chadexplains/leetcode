def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    count = 0
    max_defense = 0
    for attack, defense in properties:
        if defense < max_defense:
            count += 1
        else:
            max_defense = defense
    return count