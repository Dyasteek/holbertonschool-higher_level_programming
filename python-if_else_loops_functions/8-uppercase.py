#!/usr/bin/python3
def uppercase(str):
    upperCase = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upperCase = upperCase + chr(ord(i) - 32)
        else:
            upperCase = upperCase + i
    print('{}'.format(upperCase))
