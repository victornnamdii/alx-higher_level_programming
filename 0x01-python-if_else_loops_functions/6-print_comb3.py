#!/usr/bin/python3
for i in range(0, 90):
    if (i % 10) > (i // 10) and i < 89:
        print("{0}{1}".format((i // 10), (i % 10)), end=', ')
    elif i == 89:
        print(i)
