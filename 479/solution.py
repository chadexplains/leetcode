def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome(n):
    upper_bound = (10**n) - 1
    lower_bound = 10**(n-1)
    max_palindrome = 0
    for i in range(upper_bound**2, lower_bound**2, -1):
        if is_palindrome(i):
            for j in range(upper_bound, lower_bound-1, -1):
                if i % j == 0 and len(str(i//j)) == n:
                    return i
    return max_palindrome