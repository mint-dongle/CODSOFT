import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a tie!"
        color = "#f7b731"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        result = "Congrats! You win!"
        color = "#20bf6b"
        user_score += 1
    else:
        result = "Lol, you lose!"
        color = "#eb3b5a"
        comp_score += 1

    user_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_label.config(text=f"Computer's choice: {comp_choice.capitalize()}")
    result_label.config(text=result, bg=color)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")
    play_again_btn.config(state=tk.NORMAL)

def play_again():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="Your choice: ")
    computer_label.config(text="Computer's choice: ")
    result_label.config(text="", bg="#f5f6fa")
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")
    play_again_btn.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.configure(bg="#f5f6fa")
root.geometry("500x400")  # window size to 500x400 pixels

title_label = tk.Label(root, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 16, "bold"), bg="#f5f6fa", fg="#2d3436")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Click a button below to make your choice.", font=("Arial", 13), bg="#f5f6fa", fg="#636e72")
instruction_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#f5f6fa")
button_frame.pack(pady=10)

button_styles = {
    "rock": {"bg": "#a5a5a5", "fg": "white"},  # grey
    "paper": {"bg": "#f5f5dc", "fg": "black"},   # beige
    "scissors": {"bg": "#2d3436", "fg": "white"}   # dark grey
}

for choice in choices:
    tk.Button(
        button_frame,
        text=choice.capitalize(),
        font=("Arial", 13, "bold"),
        width=12,
        bg=button_styles[choice]["bg"],
        fg=button_styles[choice]["fg"],
        activebackground="#dff9fb",
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=10)

user_label = tk.Label(root, text="Your choice: ", font=("Arial", 12), bg="#f5f6fa")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 12), bg="#f5f6fa")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f5f6fa")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f5f6fa")
score_label.pack(pady=5)

play_again_btn = tk.Button(root, text="Play Again", font=("Arial", 12), bg="#20bf6b", fg="white", width=10, command=play_again, state=tk.DISABLED)
play_again_btn.pack(pady=5)

quit_btn = tk.Button(root, text="Quit", font=("Arial", 12), bg="#636e72", fg="white", width=10, command=root.destroy)
quit_btn.pack(pady=5)

root.mainloop()