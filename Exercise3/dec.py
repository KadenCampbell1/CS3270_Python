import functools


def track(func):
    cached = {}

    def wrapper(*args1, **args2):
        key = str(args1) + str(args2)
        if key in cached.keys():
            print(f"{args1}{args2} found in cache")
            return cached[key]
        cached[key] = func(*args1, **args2)
        wrapper.count += 1
        return cached[key]
    wrapper.count = 0
    return wrapper


def log(func):
    @functools.wraps(func)
    def wrapper(*args1, **args2):
        value = func(*args1, **args2)
        logfile = open('log.txt', 'a')
        logfile.write(f"{func.__name__}({args1}{args2}) = {value}\n")
        logfile.close()
        return value
    return wrapper


@track
@log
def fib(n):
    return n if n in (0, 1) else fib(n - 1) + fib(n - 2)


def main():
    logfile = open('log.txt', 'w')
    logfile.close()
    print(f"{fib(10)}, calls = {fib.count}")


if __name__ == "__main__":
    main()
