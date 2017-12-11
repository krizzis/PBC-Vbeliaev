# from my_app.decorators import func_args


# @func_args
def pairs(*args):

    s = 10

    length = len(args)

    for i in args:
        if type(i) not in (int, float, long):
            raise TypeError("Only list of digits accepted")

    if length <= 1:
        raise ValueError("At least 2 numbers required")

    result = []

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if args[i] + args[j] == s:
                if (args[i], args[j]) in result or (args[j], args[i]) in result:
                    break
                result.append((args[i], args[j]))
    return result
