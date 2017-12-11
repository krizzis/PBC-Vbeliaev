
def func_args(func):
    def wrapper(*args, **kwargs):
        s = ''
        for a in args:
            s += str(a) + ", "
        if kwargs is not None:
            for k, v in kwargs.items():
                s += str(k) + "=" + str(v) + ", "
        print '{}({})'.format(func.__name__, s[:-2:])
        rs = func(*args, **kwargs)
        return rs
    return wrapper
