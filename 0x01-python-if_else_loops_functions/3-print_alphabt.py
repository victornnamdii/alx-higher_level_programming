#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a != 113 and a != 101:
        print("{:c}".format(a), end='')
