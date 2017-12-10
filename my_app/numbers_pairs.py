from my_app.decorators import func_args


@func_args
def pairs(n, s=10, all_pairs=False):
    try:
        length = len(n)
    except TypeError:
        raise TypeError("Only list of digits accepted")

    for i in n:
        if type(i) not in (int, float, long):
            raise TypeError("Only list of digits accepted")

    if length <= 1:
        raise ValueError("At least 2 numbers required")

    result = []

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if n[i] + n[j] == s:
                if not all_pairs and ((n[i], n[j]) in result or (n[j], n[i]) in result):
                    break
                result.append((n[i], n[j]))
    return result
