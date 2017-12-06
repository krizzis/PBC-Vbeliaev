import argparse

parser = argparse.ArgumentParser(description="Return pairs with specified sum.")

parser.add_argument('-n', '--numbers', nargs="+", type=int, help='List of numbers to check.')
parser.add_argument('-s', '--sum', type=int, default=10, help='Optional. Sum of pairs to check. 10 by default')
parser.add_argument('-a', '--all', action='store_true',
                    help='Flag to find all possible pairs. Only unique pairs by default')
args = parser.parse_args()

n = list(args.numbers)

l = len(n)
s = args.sum
result = []

print n

for i in range(0, l-1):
    for j in range(i+1, l):
        if n[i] + n[j] == s:
            if not args.all and ([n[i], n[j]] in result or [n[j], n[i]] in result):
                break
            result.append([n[i], n[j]])

print result
