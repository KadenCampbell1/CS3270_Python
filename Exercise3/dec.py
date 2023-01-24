# @track
def fib(n):
    return n if n in (0, 1) else fib(n - 1) + fib(n - 2)


def main():
    print(fib(10), "count =", fib.count)


if __name__ == "__main__":
    main()
