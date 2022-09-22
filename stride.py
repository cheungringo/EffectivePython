from itertools import islice
# Avoid using strides when slicing
# because they make the code hard to read
# and negative strides are even worse


def main():
    test = [i for i in range(10)]
    # this is hard to read
    foo = test[1:8:2]
    print(f"{foo=}")
    # this is even harder to read
    bar = test[-2:-8:-2]
    print(f"{bar=}")

    # if you absolutely need to use strides
    # at least omit start and end and only use positive strides
    baz = test[::2]
    print(f"{baz=}")

    # Prefer splitting up slicing and then striding into two ops
    foo = test[1:8]
    foo = foo[::2]
    # However, this does do an extra shallow copy.
    # To optimize, use itertools.islice
    foo = list(islice(test, 1, 8, 2))
    print(f"{foo=}")


if __name__ == "__main__":
    main()