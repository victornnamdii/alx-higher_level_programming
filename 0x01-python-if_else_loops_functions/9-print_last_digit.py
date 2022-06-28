#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return((-1 * number) % 10)
    else:
        return(number % 10)
