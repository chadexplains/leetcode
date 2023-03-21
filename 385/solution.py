class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        curr = None
        num = ''
        sign = 1
        for c in s:
            if c == '[':
                if curr:
                    stack.append(curr)
                stack.append(c)
                curr = NestedInteger()
            elif c == ']':
                if num:
                    curr.add(NestedInteger(sign * int(num)))
                    num = ''
                    sign = 1
                if curr:
                    if len(stack) > 1:
                        prev = stack.pop()
                        stack[-1].add(curr)
                        curr = prev
                    else:
                        return curr
            elif c == '-':
                sign = -1
            elif c.isdigit():
                num += c
            elif c == ',':
                if num:
                    curr.add(NestedInteger(sign * int(num)))
                    num = ''
                    sign = 1
        if num:
            curr.add(NestedInteger(sign * int(num)))
        return curr