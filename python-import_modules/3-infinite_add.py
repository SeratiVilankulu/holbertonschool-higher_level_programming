#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    qty_args = len(sys.argv)
    result = 0

    for i in range(1, qty_args):
        result += int(sys.argv[i])
    print(result)
