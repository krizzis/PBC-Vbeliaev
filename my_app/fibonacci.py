from my_app.decorators import func_args


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
