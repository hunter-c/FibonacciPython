# Fibonacci fib
# finds fibonacci number in nth position

def fibFinder(n):

    prevPrev = 1
    prev = 1
    cur = 1

    for i in range(n - 2):
        cur = prevPrev + prev
        prevPrev = prev
        prev = cur

    return cur

dic = {}

def fibRecursive(n):
    if n in dic:
        return dic[n]

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    dic[n] = fibRecursive(n - 2) + fibRecursive(n - 1)

    return dic[n]


def power(x, n):
    H = 1
    if n == 0:
        return 1

    for i in range(n):
        H = x * H
    return H


def powerRecursive(x, n):
    if n == 0:
        return 1
    return x * powerRecursive(x, n - 1)


def mul(x, y):
    if y == 0:
        return 0
    return x + mul(x, y - 1)
