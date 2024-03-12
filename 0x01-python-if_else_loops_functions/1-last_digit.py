#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastNumber = abs(number) % 10
if number < 0:
    lastNumber *= -1
print(f"Last digit of {number:d} is {lastNumber:d}", end="")
if lastNumber > 5:
    print(" and is greater than 5")
elif lastNumber == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
