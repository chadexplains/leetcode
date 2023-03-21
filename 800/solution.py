class Solution:
    def similarRGB(self, color: str) -> str:
        def closest_hex(n):
            q, r = divmod(n, 17)
            if r > 8:
                q += 1
            return '{:02x}'.format(q * 17)
        return '#' + closest_hex(int(color[1:3], 16)) + closest_hex(int(color[3:5], 16)) + closest_hex(int(color[5:], 16))