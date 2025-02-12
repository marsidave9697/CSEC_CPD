n = int(input())
cards_str = input().split()
cards = []
for s in cards_str:
    cards.append(int(s))

left = 0
right = n - 1
sereja = 0
dima = 0
turn = 0  

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    
    if turn == 0:
        sereja += chosen
    else:
        dima += chosen
    
    turn = 1 - turn

print(sereja, dima)
