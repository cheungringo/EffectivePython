# Generator expressions can be used to replace list comprehensions
# when the list is not needed. This is especially useful when
# the list is large and the generator is used in a loop.

# Just put parentheses around the list comprehension instead of square brackets


def main():
    test = (i for i in range(10**100))

    for i in range(10):
        assert next(test) == i

    # generator expression can be composed
    # so you can pass the input of one generator
    # into another
    squares = (t**2 for t in test)
    for j in [t**2 for t in range(10, 20)]:
        assert next(squares) == j
    # the only gotcha is that generators are stateful
    # so now the advance will have the original generator at 20
    assert next(test) == 20

    # since we've already used 20
    # on test, squares will use 21
    # the next time we call next on it
    assert next(squares) == 441


if __name__ == "__main__":
    main()
