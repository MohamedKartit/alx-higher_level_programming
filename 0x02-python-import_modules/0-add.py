#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add as perf_addd
    a = 1
    b = 2
    result = perf_addd(a, b)
    print(f"{a:d} + {b:d} = {result:d}")
