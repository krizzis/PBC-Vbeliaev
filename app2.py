"""Usage:
    app2.py fib <n>
    app2.py pairs [all][<ns>...][--sum=<n>]

Commands:
    fib         Print given number of members of Fibonacci sequence
    pairs       Return pairs with specified sum.

Arguments:
   <n>          The required number of sequence members (fib)
   <ns>         List of numbers to check the sum.

Options:
  -h --help     Show this screen.
  all           Flag to find all possible pairs. Only unique pairs without it
  --sum=<n>     Sum of pairs to check. [default: 10].
"""

from docopt import docopt
from my_app.Fibonacci import fib
from my_app.Numbers_pairs import pairs


if __name__ == '__main__':
    args = docopt(__doc__)

    if args['fib']:
        print fib(int(args["<n>"]))
    elif args['pairs']:
        print pairs(list(map(int, args.get('<n>'))), int(args["--sum"]), args["all"])
