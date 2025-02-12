n = int(input())
if n == 0:
    print(0)
else:
    prev = input().strip()
    groups = 1
    prev_right = prev[1]
    for _ in range(n - 1):
        current = input().strip()
        current_left = current[0]
        if prev_right == current_left:
            groups += 1
        prev_right = current[1]
    print(groups)
