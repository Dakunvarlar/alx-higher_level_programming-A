#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv)
    sum = 0
    for i in range(1, argc):
        sum += int(sys.argv[i])
    print(sum)


if _name_ == "_main_":
    main()
