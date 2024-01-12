n = int(input())
piles = []

for _ in range(n):
    piles.append(int(input()))

ave_pile = sum(piles) // len(piles)
total_moves = sum(abs(pile - ave_pile) for pile in piles if pile > ave_pile)
print(total_moves)
