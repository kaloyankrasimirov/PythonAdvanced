import tkinter as tk
from tkinter import messagebox

class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

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



def update_ui(labels, row, col, player_num):
    color = "red" if player_num == 1 else "blue"
    labels[row][col].config(bg=color)


def reset_game(ma, labels):
    for r in range(len(ma)):
        for c in range(len(ma[0])):
            ma[r][c] = 0
            labels[r][c].config(bg="white")

def handle_column_click(ma, labels, column_num, player_num, counter, rows, cols, slots):
    try:
        row, column_num = place_player_choice(ma, column_num, player_num)
        update_ui(labels, row, column_num, player_num)

        if is_winner(ma, row, column_num, player_num, slots):
            messagebox.showinfo("Game Over!", f"The winner is {player_num}")
            reset_game(ma, labels)
            return 1,0

        counter += 1
        if counter == rows * cols:
            messagebox.showinfo("Game Over!", f"The game finished as a draw!")
            return 1, 0

        return 2 if player_num == 1 else 1, counter

    except FullColumnError:
        messagebox.showerror("Invalid move!", "The column is full!")

    return player_num, counter


def create_ui(root, rows, cols, slots_to_win):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", width=8, height=4, bg="white", relief="solid") for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r+1, column=c)

    player_state = {"player_num": 1, "counter": 0}

    def on_click(column_num, p_state):
        p_state["player_num"], p_state["counter"] = handle_column_click(matrix,
                                                                        labels,
                                                                        column_num,
                                                                        player_state["player_num"],
                                                                        player_state["counter"],
                                                                        rows,
                                                                        cols,
                                                                        slots_to_win)

    buttons = [tk.Button(root, text="⬇", width=8, height=4, bg="green",
                         command=lambda c_idx=col: on_click(c_idx, player_state))
               for col in range(cols)]
    for col, button in enumerate(buttons):
        button.grid(row=0, column=col)


def start_game():
    root = tk.Tk()
    root.title("Connect Four")

    rows, cols, slots_to_win = 6, 7, 4
    create_ui(root, rows, cols, slots_to_win)
    root.mainloop()


if __name__ == "__main__":
    start_game()