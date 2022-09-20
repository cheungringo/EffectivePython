# don't supply 0 for the start index or the length of the sequence
# for the end index.


def basic_slices():
    test = [i for i in range(10)]
    assert test[:5] == [i for i in range(5)]
    assert test[-3:] == [7, 8, 9]

# slicing is forgiving of out-of-bound indices


def out_of_bounds():
    test = [i for i in range(10)]
    assert test[20:] == []
    assert test[-11:] == test

# result of slicing list is new list
# modifying result of the slice does not modify the original list


def modify_slice():
    test = [i for i in range(10)]
    result = test[2:5]
    result[1] = 100
    assert test[1] == 1

# however, assigning to sliced ranges does modify original array
# but once again, index bonds are forgiving


def assign_slice():
    test = [i for i in range(10)]
    # the array will shrink so that the 9th index 
    # in the old array is right after 102
    test[2:9] = [100, 101, 102]
    assert test[5] == 9
    test[:] = [1]
    assert len(test) == 1
    assert test[0] == 1


if __name__ == "__main__":
    basic_slices()
    out_of_bounds()
    modify_slice()
    assign_slice()
