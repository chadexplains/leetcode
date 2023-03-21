def countSteppingNumbers(self, low: int, high: int) -> List[int]:
    def dfs(num):
        if low <= num <= high:
            res.append(num)
        if num == 0 or num > high:
            return
        last_digit = num % 10
        if last_digit == 0:
            dfs(num * 10 + 1)
        elif last_digit == 9:
            dfs(num * 10 + 8)
        else:
            dfs(num * 10 + last_digit - 1)
            dfs(num * 10 + last_digit + 1)
    res = []
    for i in range(10):
        dfs(i)
    return sorted(res)