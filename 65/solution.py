class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        if s[0] in "+-":
            s = s[1:]
        if not s or s == ".":
            return False
        if "e" in s:
            s1, s2 = s.split("e")
            if not s1 or not s2 or "." in s2:
                return False
            if s1[0] in "+-":
                s1 = s1[1:]
            if not s1 or s1 == ".":
                return False
            if s2[0] in "+-":
                s2 = s2[1:]
            if not s2 or not s2.isdigit():
                return False
            s = s1 + s2
        if "." in s:
            if s.count(".") > 1:
                return False
            s1, s2 = s.split(".")
            if not s1 and not s2:
                return False
            if s1 and s1[0] in "+-":
                s1 = s1[1:]
            if s2 and s2[-1] in "+-":
                s2 = s2[:-1]
            if not s1 and not s2:
                return False
            if s1 and not s1.isdigit():
                return False
            if s2 and not s2.isdigit():
                return False
        else:
            if not s.isdigit():
                return False
        return True