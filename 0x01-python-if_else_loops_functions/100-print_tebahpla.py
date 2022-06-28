#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if (a % 2) != 0:
        a = a - (ord('a') - ord('A'))
    print("{:c}".format(a), end='')
