class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr_str = ''
                while stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                stack.pop()
                curr_num = ''
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                stack.append(curr_str * int(curr_num))
        return ''.join(stack)