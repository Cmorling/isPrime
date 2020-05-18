import sys
import time

def fastPrime(input):
    for i in range(2, int(input ** (1/2)) + 1):
        if (input % i) == 0:
            print("{} is not a prime number.".format(input))
            return
    print("{} is a prime number.".format(input))

def slowPrime(input):
    factors = []
    for i in range(1, input + 1):
        if (input % i) == 0:
            factors.append(i)
    if len(factors) == 2:
        print("{} is a prime number.".format(input))
    else:
        print("Know factors for integer {} are {}".format(input, factors))
def endProgram(start, end):
    print("Program ran in {} seconds.".format(round(end - start, 4)))
def __main__():
    startTime = time.time()
    if len(sys.argv) < 3:
        print("Usage: python3 main.py [flag] [integer]")
        print("Flags")
        print("\t -f: Fast method")
        print("\t -s: Slow method")
        exit()
    elif sys.argv[1] == "-f":
        fastPrime(int(sys.argv[2]))
    elif sys.argv[1] == "-s":
        slowPrime(int(sys.argv[2]))
    else: 
        print("Wrong flag supplied")
    endProgram(startTime, time.time())
__main__()