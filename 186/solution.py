def reverseWords(self, s: List[str]) -> None:
    
    def reverse(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    # Reverse the entire array
    reverse(s, 0, len(s) - 1)
    
    # Reverse each word individually
    start = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse(s, start, i - 1)
            start = i + 1
    
    # Reverse the last word
    reverse(s, start, len(s) - 1)