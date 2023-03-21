def ipToCIDR(ip: str, n: int) -> List[str]:
    def ipToInt(ip: str) -> int:
        return sum([int(x) << (24 - i * 8) for i, x in enumerate(ip.split('.'))])
    
    def intToIP(n: int) -> str:
        return '.'.join([str(n >> (24 - i * 8) & 255) for i in range(4)])
    
    def numTrailingZeros(n: int) -> int:
        count = 0
        while n & 1 == 0:
            count += 1
            n >>= 1
        return count
    
    result = []
    start = ipToInt(ip)
    while n > 0:
        mask = max(33 - numTrailingZeros(start), 33 - numTrailingZeros(n))
        result.append(intToIP(start) + '/' + str(mask))
        start += 1 << (32 - mask)
        n -= 1 << (32 - mask)
    return result