def minSwaps(data):
    ones = sum(data)
    window = data[:ones]
    max_ones = window.count(1)
    ones_in_window = max_ones
    for i in range(ones, len(data)):
        ones_in_window += data[i] - data[i-ones]
        max_ones = max(max_ones, ones_in_window)
    return ones - max_ones}