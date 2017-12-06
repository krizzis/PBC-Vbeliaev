import argparse
from Decorators import func_args


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Return pairs with specified sum.")

    parser.add_argument('-n', '--numbers', nargs="+", type=int, help='List of numbers to check.')
    parser.add_argument('-s', '--sum', type=int, default=10, help='Optional. Sum of pairs to check. 10 by default')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Flag to find all possible pairs. Only unique pairs by default')
    args = parser.parse_args()

    pairs(args.numbers, args.sum, args.all)
