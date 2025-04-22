import tkinter as tk
from tkinter import messagebox, simpledialog

# Global variables
player_scores = {"X": 0, "O": 0}
current_player = "X"
player_names = {"X": "Player 1", "O": "Player 2"}

# Functions
def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            for button in buttons:
                button.config(state=tk.DISABLED)
            messagebox.showinfo("Winner", f"{buttons[combo[0]]['text']} ({player_names[buttons[combo[0]]['text']]}) wins!")
            update_score(buttons[combo[0]]["text"])
            return
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Draw", "It's a draw!")
        for button in buttons:
            button.config(state=tk.DISABLED)

def button_click(index):
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    update_label()

def update_label():
    label.config(text=f"{player_names[current_player]}'s turn")

def update_score(winner):
    player_scores[winner] += 1
    score_label.config(text=f"X: {player_scores['X']} | O: {player_scores['O']}")

def reset_game():
    global current_player
    current_player = "X"
    label.config(text=f"{player_names[current_player]}'s turn")
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")

# Setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Get player names
player_names["X"] = simpledialog.askstring("Player X", "Enter Player 1's name:", parent=root) or "Player 1"
player_names["O"] = simpledialog.askstring("Player O", "Enter Player 2's name:", parent=root) or "Player 2"

# UI Elements
buttons = [tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(root, text=f"{player_names[current_player]}'s turn", font=("Arial", 20))
label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text=f"X: {player_scores['X']} | O: {player_scores['O']}", font=("Arial", 15))
score_label.grid(row=4, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 15), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

# Start the game
root.mainloop()