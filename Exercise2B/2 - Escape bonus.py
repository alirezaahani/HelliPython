table = [
    ['F', 'F', 'F', 'X', 'F', 'F'],
    ['F', 'F', 'M', 'X', 'X', 'W'],
    ['F', 'M', 'X', 'X', 'X', 'X'],
    ['F', 'X', 'X', 'X', 'X', 'F'],
    ['F', 'X', 'M', 'F', 'X', 'F'],
    ['F', 'F', 'F', 'F', 'X', 'M'],
]

player_x = 0
player_y = 0
health = 1

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

  if player_x > 5 or player_x < 0 or player_y > 5 or player_y < 0:
    print('N')
    break

  if table[player_y][player_x] == 'X':
    health -= 1

  if table[player_y][player_x] == 'M':
    health += 1

  if health < 1:
    print('L')
    break

  if table[player_y][player_x] == 'W':
    print('W')
    break
