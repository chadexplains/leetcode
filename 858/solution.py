class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // math.gcd(p, q)
        reflections = lcm // q
        if reflections % 2 == 0:
            return 2
        else:
            return 1 if (lcm // p) % 2 == 0 else 0
