#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0  
    romanums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    translated = 0    
    for char in roman_string:
        actual = romanums[char]   
        if actual > translated:
            total += actual - 2 * translated
        else:
            total += actual
        
        translated = actual  
    return total
