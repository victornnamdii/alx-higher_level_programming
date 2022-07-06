#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
             'I': 1, 'Z': 0}
    total = 0
    if (isinstance(roman_string, str)):
        i = 0
        while i < len(roman_string):
            f = roman_string[i]
            if (i + 1) < len(roman_string):
                n = roman_string[i + 1]
            else:
                n = 'Z'
            if int(roman[f]) < int(roman[n]) and n != 'Z':
                total += (int(roman[n]) - int(roman[f]))
                i += 2
            else:
                total += int(roman[f])
                i += 1
        return(total)
    return(0)
