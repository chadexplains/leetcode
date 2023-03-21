def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    prefix_sum = [0] * (n + 1)
    for booking in bookings:
        start, end, seats = booking
        prefix_sum[start - 1] += seats
        prefix_sum[end] -= seats
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]
    return prefix_sum[:-1]