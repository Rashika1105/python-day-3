import sys

#!/usr/bin/env python3
"""
Simple factorial program.

Usage:
    python3 untitled_factorial.py [n]

If n is omitted, the program will prompt for input.
"""
def factorial(n: int) -> int:
        if n < 0:
                raise ValueError("factorial() not defined for negative values")
        result = 1
        for i in range(2, n + 1):
                result *= i
        return result

def parse_int(s: str) -> int:
        try:
                return int(s)
        except ValueError:
                raise ValueError("please provide an integer")

if __name__ == "__main__":
        if len(sys.argv) > 1:
                arg = sys.argv[1]
        else:
                arg = input("Enter a non-negative integer: ").strip()
        n = parse_int(arg)
        print(f"{n}! = {factorial(n)}")