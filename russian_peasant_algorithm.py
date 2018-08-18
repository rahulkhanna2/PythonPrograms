# Simple Algorthim which takes two numbers and multiply it without math table
# Requirements: multiply smaller number by 2 and divide bigger number by 2
# Add the numbers

"""
24 X 16 = ?
12   32 # Not needed since first number is even
6    64
3    128 # Needed since first number is 3 (odd)
1    256


"""

import time

x = int(raw_input("Enter your first number: "))
y = int(raw_input("Enter your second number: "))


def russian(x,y):
    total, table = 0, {}
    if x % 2 != 0: table = {x: y}  # if the first number is odd add y
    while x > 0:
        x, y = x / 2, y * 2
        table[x] = y
    for key, value in table.iteritems():
        if key % 2 == 1: total += value

    return total


def test_russian():
	start_time = time.time()
	print russian(x, y)
	end_time = time.time()
	print "Russian Peasant Algorithm took %f seconds" % (end_time - start_time)


test_russian()


