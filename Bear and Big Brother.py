a_and_b = input().split()
a = int(a_and_b[0])
b = int(a_and_b[1])

years = 0

while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)
