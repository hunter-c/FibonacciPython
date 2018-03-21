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
