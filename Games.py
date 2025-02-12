n = int(input())
teams = []
for _ in range(n):
    h, a = input().split()
    h = int(h)
    a = int(a)
    teams.append((h, a))

count = 0
for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            count += 1

print(count)
