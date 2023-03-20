```def read(self, buf, n):
    total = 0
    buffer = [''] * 4
    while total < n:
        count = read4(buffer)
        if not count:
            break
        for i in range(min(count, n - total)):
            buf[total] = buffer[i]
            total += 1
    return total```