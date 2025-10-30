def is_palindrome(n):
    def backword(j):
        j=str(j)
        return  int(j[::-1])
    return n==backword(n)
