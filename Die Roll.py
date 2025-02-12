input_values = input().split()
Y = int(input_values[0])
W = int(input_values[1])

max_roll = max(Y, W)

favorable = 6 - max_roll + 1

from math import gcd
common_divisor = gcd(favorable, 6)
numerator = favorable // common_divisor
denominator = 6 // common_divisor

print(f"{numerator}/{denominator}")
