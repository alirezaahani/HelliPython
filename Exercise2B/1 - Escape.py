
table = [
    ['F', 'F', 'F', 'X', 'F'],
    ['X', 'F', 'X', 'F', 'F'],
    ['F', 'F', 'X', 'F', 'W'],
    ['F', 'X', 'X', 'F', 'F'],
    ['F', 'F', 'F', 'F', 'F'],
]

player_x = 0
player_y = 0

actions = input().split(',')

for action in actions:
  action = action.strip()

  if action == 'R':
    player_x += 1
  elif action == 'L':
    player_x -= 1
  elif action == 'U':
    player_y -= 1
  elif action == 'D':
    player_y += 1

  if player_x > 4 or player_x < 0 or player_y > 4 or player_y < 0:
    print('N')
    break

  if table[player_y][player_x] == 'X':
    print('L')
    break

  if table[player_y][player_x] == 'W':
    print('W')
    break
