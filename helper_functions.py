# Prefer helper functions over complicated one line expressions


def less_readable():
    """Although Python syntax allows code like this to be written
    in one line, it's not very readable"""
    my_values = {'red': ['5'], 'green': [''], 'blue': ['0']}
    red = int(my_values.get('red', [''])[0] or 0)
    green = int(my_values.get('green', [''])[0] or 0)
    opacity = int(my_values.get('opacity', [''])[0] or 0)
    return red, green, opacity


def more_readable():
    """Breaking up the code into a helper function with if-else
    statements makes it way more clear what's happening."""
    my_values = {'red': ['5'], 'green': [''], 'blue': ['0']}

    def get_first_int(values, key, default=0):
        found = values.get(key, [''])
        if found[0]:
            return int(found[0])
        return default
    red = get_first_int(my_values, 'red')
    green = get_first_int(my_values, 'green')
    opacity = get_first_int(my_values, 'opacity')
    return red, green, opacity


if __name__ == "__main__":
    print(less_readable())
    print(more_readable())
