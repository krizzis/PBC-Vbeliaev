import argparse
from my_app.Fibonacci import fib
from my_app.Numbers_pairs import pairs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="App can return a Fibonacci sequence with given length "
                                                 "or find numbers pair with  specified sum")

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_fib = subparsers.add_parser('fib', help='Print given number of members of Fibonacci sequence')
    parser_fib.add_argument("number", help="The required number of sequence members", type=int)
    parser_fib.set_defaults(which='fib')

    parser_pairs = subparsers.add_parser('pairs', help='Return pairs with specified sum.')
    parser_pairs.add_argument('-n', '--numbers', nargs="+", type=int, help='List of numbers to check.')
    parser_pairs.add_argument('-s', '--sum', type=int, default=10,
                              help='Optional. Sum of pairs to check. 10 by default')
    parser_pairs.add_argument('-a', '--all', action='store_true',
                              help='Flag to find all possible pairs. Only unique pairs by default')
    parser_pairs.set_defaults(which='pairs')

    args = parser.parse_args()

    if args.which == 'fib':
        fib(args.number)
    elif args.which == 'pairs':
        pairs(args.numbers, args.sum, args.all)



