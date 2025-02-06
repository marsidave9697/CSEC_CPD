first_line = input().split()
n = int(first_line[0])
h = int(first_line[1])

second_line = input().split()

total_width = 0

for height_str in second_line:
    height = int(height_str)
    if height > h:
        total_width += 2
    else:
        total_width += 1

print(total_width)
