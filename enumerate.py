# Prefer enumerate to range


def main():
    test = ["red", "blue", "green"]
    # bad loop
    for i in range(len(test)):
        print(f"{i}: {test[i]}")
    
    # good loop
    for i, color in enumerate(test):
        print(f"{i}: {color}")
    
    # if you want to start with a different
    # starting value of i but still go through the
    # entire list, use enumerate with a start value
    for i, color in enumerate(test, 1):
        print(f"{i}: {color}")


if __name__ == "__main__":
    main()