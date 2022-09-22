# Prefer list comprehensions over map and filter


def main():
    test = [i for i in range(10)]

    squares_bad = list(map(lambda x: x**2, test))
    squares = [t**2 for t in test]

    assert squares_bad == squares

    even_squares_bad = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, test)))
    even_squares = [t**2 for t in test if t % 2 == 0]

    assert even_squares_bad == even_squares


def max_two_expressions_per_list_comp():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    assert flat == [i for i in range(1, 10)]
    # example of bad is when you try to add a third expression
    # to the matrix

    bad = [x for row in matrix for x in row if x % 2 == 0]
    better = []
    for row in matrix:
        better.extend([x for x in row if x % 2 == 0])
    assert bad == better


if __name__ == "__main__":
    main()
    max_two_expressions_per_list_comp()
