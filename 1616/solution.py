def checkPalindromeFormation(a: str, b: str) -> bool:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    i, j = 0, len(a) - 1
    while i < j and a[i] == b[j]:
        i, j = i + 1, j - 1
    return is_palindrome(a[i:j+1]) or is_palindrome(b[i:j+1]) or is_palindrome(a[i:j+1] + b[i:j+1][::-1]) or is_palindrome(b[i:j+1] + a[i:j+1][::-1])