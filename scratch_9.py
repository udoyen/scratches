#!/usr/bin/env python3

if __name__ == "__main__":
    import sys
    print(len(sys.argv))
    if (len(sys.argv) - 1) == 1:
        print("0", end=" ")
        print('')
    elif (len(sys.argv) - 1) == 2:
        print("{:d}".format(int(sys.argv[1])), end="")
        print('')
    else:
        num = sys.argv
        sum = 0
        for i in range(1, len(num)):
            sum += int(num[i])
        print("{:d}".format(sum), end="")
        print('')