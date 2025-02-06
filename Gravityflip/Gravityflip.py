n = int(input())

cube_counts = input().split()

a = []
for count in cube_counts:
    a.append(int(count))

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

for count in a:
    print(count, end=' ')
print()
