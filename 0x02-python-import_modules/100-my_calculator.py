#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    op = {"+": add, "-": sub, "*": mul, "/": div}
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} + {}".format(a, sys.argv[2], b, op[sys.arv[2]](a, b)))
