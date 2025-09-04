#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 3:
        print('{}'.format(int(sys.argv[1]) + int(sys.argv[2])))
