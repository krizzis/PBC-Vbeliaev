"""Usage:
    app_docopt.py fib <number>
    app_docopt.py pairs <numbers>...
"""
from docopt import docopt
from my_app.Numbers_pairs import pairs


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

    for i in arguments.get("numbers"):
        print i
    # pairs())
