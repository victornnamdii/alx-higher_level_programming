#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = -1 * ((-1 * number) % 10)
else:
    ldigit = number % 10
first_string = f"Last digit of {number} is {ldigit}"
if ldigit > 5:
    print(f"{first_string} and is greater than 5")
elif ldigit == 0:
    print(f"{first_string} and is 0")
elif ldigit < 6 and ldigit != 0:
    print(f"{first_string} and is less than 6 and not 0")
