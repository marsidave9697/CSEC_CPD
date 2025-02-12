n = int(input())

birds_input = input().strip().split()
birds = [int(birds_input[i]) for i in range(n)]

m = int(input())

for _ in range(m):
    x, y = input().strip().split()
    x = int(x) - 1 
    y = int(y)
    if x > 0:
        birds[x - 1] += y - 1
    if x < n - 1:
        birds[x + 1] += birds[x] - y
    birds[x] = 0

for count in birds:
    print(count)
