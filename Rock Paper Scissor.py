import tkinter as tk
import random

options = ['rock', 'paper', 'scissors']

def get_result(player, cpu):
    if player == cpu:
        return "It's a tie!"
    if (player == 'rock' and cpu == 'scissors') or \
       (player == 'paper' and cpu == 'rock') or \
       (player == 'scissors' and cpu == 'paper'):
        return "You win!"
    return "Computer wins!"

def make_choice(player_pick):
    cpu_pick = random.choice(options)
    player_text.config(text=f"Your choice: {player_pick}")
    cpu_text.config(text=f"Computer: {cpu_pick}")
    result_text.config(text=get_result(player_pick, cpu_pick))

win = tk.Tk()
win.title("RPS Game")
win.geometry("320x260")
win.resizable(0, 0)

heading = tk.Label(win, text="Rock - Paper - Scissors", font=("Helvetica", 15, "bold"))
heading.pack(pady=15)

player_text = tk.Label(win, text="", font=("Helvetica", 12))
player_text.pack()

cpu_text = tk.Label(win, text="", font=("Helvetica", 12))
cpu_text.pack()

result_text = tk.Label(win, text="", font=("Helvetica", 13, "bold"), fg="green")
result_text.pack(pady=12)

btns = tk.Frame(win)
btns.pack()

tk.Button(btns, text="Rock", width=9, command=lambda: make_choice('rock')).grid(row=0, column=0, padx=6)
tk.Button(btns, text="Paper", width=9, command=lambda: make_choice('paper')).grid(row=0, column=1, padx=6)
tk.Button(btns, text="Scissors", width=9, command=lambda: make_choice('scissors')).grid(row=0, column=2, padx=6)

win.mainloop()
