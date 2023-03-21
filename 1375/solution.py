def numTimesAllBlue(light):
    max_index = 0
    moments = 0
    for i, bulb in enumerate(light):
        max_index = max(max_index, bulb)
        if max_index == i + 1:
            moments += 1
    return moments