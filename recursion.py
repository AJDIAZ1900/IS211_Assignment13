def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 == s2:
        return 0

    if s1 < s2:
        return -1

    return 1