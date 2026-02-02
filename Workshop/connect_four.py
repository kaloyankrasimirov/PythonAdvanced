class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

def print_matrix(board):
    for row in board:
        print(row)

def valid_column(col, max_index):
    if not (0 <= col < max_index):
        raise InvalidColumnError

def place_player_choice(board, c, player_mark):
    for r in range(len(board) -1, -1, -1):
        if board[r][c] == 0:
            board[r][c] = player_mark
            return r, c
    raise FullColumnError

def is_player_num(board, r, c, p_marker):
    try:
        return board[r][c] == p_marker
    except IndexError:
        return False

def vertical_win(board, r, c, player_marker, streak):
    return all(is_player_num(board, r + idx, c, player_marker) for idx in range(streak))

def horizontal_win(board, r, c, player_marker, streak):
    filled = 1
    for idx in range(1, streak):
        if is_player_num(board, r, c + idx, player_marker):
            filled += 1
        else:
            break

    for idx in range(1, streak):
        if is_player_num(board, r, c - idx, player_marker):
            filled += 1
        else:
            break

    return filled >= streak

def left_diagonal_win(board, r, c, player_marker, streak):
    filled = 1

    for idx in range(1, streak):
        if is_player_num(board, r + idx, c + idx, player_marker):
            filled += 1
        else:
            break

    for idx in range(1, streak):
        if is_player_num(board, r - idx, c - idx, player_marker):
            filled += 1
        else:
            break

    return filled >= streak


def right_diagonal_win(board, r, c, player_marker, streak):
    filled = 1

    for idx in range(1, streak):
        if is_player_num(board, r + idx, c - idx, player_marker):
            filled += 1
        else:
            break

    for idx in range(1, streak):
        if is_player_num(board, r - idx, c + idx, player_marker):
            filled += 1
        else:
            break

    return filled >= streak


def is_winner(board, r, c, player_marker, streak):
    return (
        vertical_win(board, r, c, player_marker, streak) or
        horizontal_win(board, r, c, player_marker, streak) or
        left_diagonal_win(board, r, c, player_marker, streak) or
        right_diagonal_win(board, r, c, player_marker, streak)
    )

STREAK = 4
row_count = 6
cols_count = 7

matrix = create_matrix(row_count, cols_count)
print_matrix(matrix)

player_num = 1
counter = 0

while True:
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        valid_column(column_num, cols_count)
        row, col = place_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)
    except ValueError:
        print(f"Please enter a valid number between 1 and {cols_count}.")
        continue
    except InvalidColumnError:
        print(f"Please enter a valid number between 1 and {cols_count}.")
        continue
    except FullColumnError:
        print("This column is already full! Please, chose another column.")
        continue

    if is_winner(matrix, row, col, player_num, STREAK):
        print(f"Congratulations! The winner is: {player_num}! ")
        break

    counter += 1
    if row_count * cols_count == counter:
        print("The game finished as a draw!")
        break

    player_num = 2 if player_num == 1 else 1

