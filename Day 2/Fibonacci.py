import sys


def fib(n):
    try:
        if type(n) is not int or n <= 0:
            raise ValueError
    except ValueError:
        print "ERROR: Number must be a positive"
        sys.exit(1)

    a1, a2 = 0, 1
    res = []
    for _ in range(n):
        s = a1
        a1 = a2
        a2 += s
        res.append(s)
    return res


print fib(5)