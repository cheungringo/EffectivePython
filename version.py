# know which version of python is running
# can use
# > python --version
# prefer python3 since development is frozen on python2

import sys


if __name__ == "__main__":
    print(sys.version)
    print(sys.version_info)
