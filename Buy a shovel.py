input_values = input().split()
k = int(input_values[0])
r = int(input_values[1])

shovels = 1
while True:
    total_cost = shovels * k
    if total_cost % 10 == 0 or total_cost % 10 == r:
        print(shovels)
        break
    shovels += 1
