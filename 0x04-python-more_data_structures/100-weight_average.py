#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        hold = dict(my_list)
        total = 0
        divisor = 0
        for keys in hold:
            total += (int(keys) * int(hold[keys]))
            divisor += int(hold[keys])
        return(total / divisor)
    return(0)
