row_of_one = 0
col_of_one = 0

for i in range(1, 6): 
    row_input = input().strip()
    for j in range(1, 6):  
        value = int(row_input.split()[j - 1])
        if value == 1:
            row_of_one = i
            col_of_one = j

moves = abs(row_of_one - 3) + abs(col_of_one - 3)

print(moves)
