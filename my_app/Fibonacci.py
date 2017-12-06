import argparse
from Decorators import func_args


@func_args
def fib(n):
    if n <= 0:
        raise ValueError("Number must be a positive")

    a1, a2 = 0, 1
    res = []
    for _ in range(n):
        s = a1
        a1 = a2
        a2 += s
        res.append(s)

    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Print given number of members of Fibonacci sequence")
    parser.add_argument("number", help="The required number of sequence members", type=int)
    args = parser.parse_args()

    fib(int(args.number))