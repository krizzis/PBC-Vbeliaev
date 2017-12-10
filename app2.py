"""Usage:
    app2.py fib <n>
    app2.py pairs <ns>...

Commands:
    fib         Print given number of members of Fibonacci sequence
    pairs       Return pairs with specified sum.

Arguments:
   <n>          The required number of sequence members (fib)
   <ns>         List of numbers to check the sum.

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
from my_app.fibonacci import fib
from my_app.numbers_pairs import pairs


if __name__ == '__main__':
    args = docopt(__doc__)

    if args['fib']:
        print fib(int(args["<n>"]))
    elif args['pairs']:
        print pairs(*list(map(int, args["<ns>"])))
