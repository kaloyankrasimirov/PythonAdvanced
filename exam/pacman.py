n = int(input())

field = []
pacman = []
health = 100
total_stars = 0
collected_stars = 0
immunity = False

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == "P":
            pacman = [row, col]
        elif field[row][col] == "*":
            total_stars += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

def get_new_pos(r, c, a_command, n_field):
    move_r, move_c = directions[a_command]
    return (r + move_r) % n_field, (c + move_c) % n_field

while True:
  command = input()

  if command == "end":
      print("Pacman failed to collect all the stars.")
      field[new_r][new_c] = "P"
      break


  move_row, move_col = directions[command]
  field[pacman[0]][pacman[1]] = "-"
  new_r, new_c = get_new_pos(pacman[0], pacman[1], command, n)
  pacman = [new_r, new_c]
  symbol = field[new_r][new_c]

  if symbol == "*":
      collected_stars += 1
      if collected_stars == total_stars:
          print("Pacman wins! All the stars are collected.")
          field[new_r][new_c] = "P"
          break

  elif symbol == "F":
      immunity = True

  elif symbol == "G":
      if immunity:
          immunity = False
      else:
          health -= 50
          if health <= 0:
              print(f"Game over! Pacman last coordinates [{new_r},{new_c}]")
              field[new_r][new_c] = "P"
              break

  field[new_r][new_c] = "-"

print(f"Health: {health}")
if collected_stars < total_stars:
    print(f"Uncollected stars: {total_stars - collected_stars}")
for row in field:
    print(''.join(row))

