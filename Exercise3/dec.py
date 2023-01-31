import functools


def trace(f):
    @functools.wraps(f)
    def wrapper(*args1, **args2):
        print(f.__name__, 'with', args1, args2)
        return f(*args1, **args2)
    return wrapper


@trace
def fib(n):
    return n if n in (0, 1) else fib(n - 1) + fib(n - 2)


def main():
    # print(fib(10), "count =", fib.count)
    print(fib(7))


if __name__ == "__main__":
    main()
