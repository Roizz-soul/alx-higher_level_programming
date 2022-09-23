#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[i]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for h in range(len(sys.argv) - 1):
            print("{}: {}".format(h + 1, sys.argv[h + 1]))
