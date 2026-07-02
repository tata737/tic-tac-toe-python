import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

# ===================== BACKGROUND =====================
root.configure(bg="#DDE6ED")

main_frame = tk.Frame(root, bg="#DDE6ED")
main_frame.pack(expand=True)

# ===================== WINDOW =====================
window_width = 420
window_height = 520

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ===================== TITLE CARD =====================
title_frame = tk.Frame(main_frame, bg="#27374D", bd=0)
title_frame.grid(row=0, column=0, columnspan=3, pady=(10, 10))

title_label = tk.Label(
    title_frame,
    text="⭕ Tic Tac Toe ✖",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#27374D",
    pady=10
)
title_label.pack()

# ===================== GAME STATE =====================
current_player = "X"
game_over = False
x_score = 0
o_score = 0
buttons = []

# ===================== SCORE CARD =====================
score_frame = tk.Frame(main_frame, bg="#9DB2BF", pady=8)
score_frame.grid(row=1, column=0, columnspan=3, pady=10)

score_label = tk.Label(
    score_frame,
    text="Player X : 0   |   Player O : 0",
    font=("Segoe UI", 12, "bold"),
    bg="#9DB2BF",
    fg="#1B1B1B"
)
score_label.pack()

# ===================== TURN LABEL =====================
player_label = tk.Label(
    main_frame,
    text="Turn : X",
    font=("Segoe UI", 13, "bold"),
    bg="#DDE6ED",
    fg="#27374D"
)
player_label.grid(row=2, column=0, columnspan=3, pady=5)

# ===================== LOGIC =====================
def show_result(text):
    messagebox.showinfo("Game Over", text)


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"], [(i,0),(i,1),(i,2)]

    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return buttons[0][j]["text"], [(0,j),(1,j),(2,j)]

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"], [(0,0),(1,1),(2,2)]

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"], [(0,2),(1,1),(2,0)]

    return None, []


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True


def button_click(row, col):
    global current_player, game_over, x_score, o_score

    if game_over or buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player
    buttons[row][col]["fg"] = "#1B1B1B"

    winner, cells = check_winner()

    if winner:
        game_over = True

        if winner == "X":
            x_score += 1
        else:
            o_score += 1

        score_label.config(
            text=f"Player X : {x_score}   |   Player O : {o_score}"
        )

        for r, c in cells:
            buttons[r][c]["bg"] = "#A8DF8E"

        show_result(f"Player {winner} Wins!")

        for i in range(3):
            for j in range(3):
                buttons[i][j]["state"] = "disabled"
        return

    if check_draw():
        game_over = True
        show_result("Draw!")

        for i in range(3):
            for j in range(3):
                buttons[i][j]["state"] = "disabled"
        return

    current_player = "O" if current_player == "X" else "X"
    player_label.config(text=f"Turn : {current_player}")


# ===================== BUTTONS =====================
def restart_game():
    global current_player, game_over

    current_player = "X"
    game_over = False
    player_label.config(text="Turn : X")

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="white", state="normal")


def reset_score():
    global x_score, o_score

    x_score = 0
    o_score = 0
    score_label.config(text="Player X : 0   |   Player O : 0")


# ===================== HOVER =====================
def on_enter(event):
    if event.widget["text"] == "":
        event.widget["bg"] = "#E3F2FD"


def on_leave(event):
    if event.widget["text"] == "":
        event.widget["bg"] = "white"


# ===================== BOARD =====================

def create_board():
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(
                main_frame,
                text="",
                font=("Segoe UI", 24, "bold"),
                width=4,
                height=1,
                bg="white",
                relief="flat",
                cursor="hand2",
                command=lambda r=i, c=j: button_click(r, c)
            )

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            btn.grid(row=i+3, column=j, padx=5, pady=5)
            row.append(btn)

        buttons.append(row)


create_board()

# ===================== CONTROL PANEL =====================
control_frame = tk.Frame(main_frame, bg="#DDE6ED")
control_frame.grid(row=7, column=0, columnspan=3, pady=15)

tk.Button(
    control_frame,
    text="Restart Game",
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=restart_game,
    width=12
).grid(row=0, column=0, padx=5)

tk.Button(
    control_frame,
    text="Reset Score",
    bg="#FF9800",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=reset_score,
    width=12
).grid(row=0, column=1, padx=5)

root.mainloop()