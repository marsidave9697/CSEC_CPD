s = input().strip()
current = 'a'
total_rotations = 0

for char in s:
    current_pos = ord(current) - ord('a')
    next_pos = ord(char) - ord('a')
    
    clockwise = (next_pos - current_pos) % 26
    counterclockwise = (current_pos - next_pos) % 26
    
    total_rotations += min(clockwise, counterclockwise)
    
    current = char

print(total_rotations)
