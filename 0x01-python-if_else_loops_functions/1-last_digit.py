#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# To access the last digit of number which is an integer,
# we first get its string representation
# then we access last string,
# afterwards we convert it to integer

last = int(repr(number)[-1])
if last > 5:
    print(f'Last digit of {number} is {last} and is greater than 5')
elif last == 0:
    print(f'Last digit of {number} is {last} and is 0')
elif last < 6 and last != 0:
    print(f'Last digit of {number} is {last} and is less than 6 and not 0')
