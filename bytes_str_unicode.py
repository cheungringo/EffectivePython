# In Python 3:
# bytes contain raw 8-bit values
# str contains Unicode characters

# In Python 2:
# str contains raw 8-bit values
# unicode contains Unicode characters


# do the encoding and decoding at the edges of your system
# and only work with str inside your program


def to_str(bytes_or_str) -> str:
    """Convert bytes or str to str"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str) -> bytes:
    """Convert bytes or str to bytes"""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


def test_to_str_to_bytes() -> None:
    """Convert between string and bytes"""
    string = "hello"
    str_as_bytes = to_bytes(string)
    assert string == to_str(str_as_bytes)
    assert to_bytes(str_as_bytes) == str_as_bytes


# writing and reading from files in Python 3 expects
# str, not bytes. You need to specify binary mode like so:

# with open("somefile.bin", "wb") as f:
# if you want to write byte data in Python3


if __name__ == "__main__":
    test_to_str_to_bytes()
