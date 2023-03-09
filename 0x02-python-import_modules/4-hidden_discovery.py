#!/usr/bin/python3
import hidden_4


def main():
    file = dir(hidden_4)
    length = len(file)
    for i in range(0, length):
        if file[i][0:2] != "_":
            print(file[i])

if _name_ == "_main_":
    main()
