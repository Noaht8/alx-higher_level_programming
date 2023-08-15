#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Get all arguments except the script name
    result = sum(int(arg) for arg in args)  # Convert each argument to an integer and sum them

    print(result)
