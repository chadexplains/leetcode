def maximumSwap(num):
    digits = list(map(int, str(num)))
    max_digit = -1
    max_index = -1
    left_index = -1
    right_index = -1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > max_digit:
            max_digit = digits[i]
            max_index = i
        elif digits[i] < max_digit:
            left_index = i
            right_index = max_index
    if left_index != -1:
        digits[left_index], digits[right_index] = digits[right_index], digits[left_index]
    return int(''.join(map(str, digits)))