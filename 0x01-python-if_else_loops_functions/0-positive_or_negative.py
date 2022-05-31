#!/bin/python3
import random
number = random.randint(-10, 10)

# initialize if else conditional statement
if number > 0:
    print(f'{number} is positive')
elif number == 0:
    print(f'{number} is zero')
elif number < 0:
    print(f'{number} is negative')
