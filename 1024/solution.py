def videoStitching(clips, T):
    clips.sort()
    max_end = 0
    count = 0
    i = 0
    while i < len(clips) and max_end < T:
        if clips[i][0] > max_end:
            return -1
        curr_end = max(clips[j][1] for j in range(i, len(clips)) if clips[j][0] <= max_end)
        count += 1
        max_end = curr_end
        i = j + 1
    return count if max_end >= T else -1