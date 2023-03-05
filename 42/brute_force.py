def trap(height):
    n = len(height)
    trapped_water = 0
    for i in range(1, n-1):
        max_left, max_right = 0, 0
        for j in range(i+1):
            max_left = max(max_left, height[j])
        for j in range(i, n):
            max_right = max(max_right, height[j])
        trapped_water += min(max_left, max_right) - height[i]
    return trapped_water
