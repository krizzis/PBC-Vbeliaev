import argparse
import sys

parser = argparse.ArgumentParser(description="Print given number of members of Fibonacci sequence")
parser.add_argument("number", help="The required number of sequence members", type=int)
args = parser.parse_args()

try:
    n = int(args.number)
    if n <= 0:
        raise ValueError
except ValueError:
    print "Number must be a positive"
    sys.exit()

a1, a2 = 0, 1
for _ in range(n):
    s = a1
    a1 = a2
    a2 += s
    print s
