#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))
