#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    qty_args = len(sys.argv)

# to print the header
    print("{:d} argument".format(qty_args - 1), end="")
    if (qty_args != 2):
        print("s", end="")
    if (qty_args > 1):
        print(":")
    if (qty_args == 1):
        print(".")

# to print all the args
    for i in range(1, qty_args):
        print("{:d}: {}".format(i, sys.argv[i]))
