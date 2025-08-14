import tkinter as tk
import random

# Choices
CHOICES = ["Rock", "Paper", "Scissors"]

# Game logic
def get_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Button callback
def play(player_choice):
    computer_choice = random.choice(CHOICES)
    result = get_winner(player_choice, computer_choice)
    result_label.config(text=f"Your choice: {player_choice}\n"
                             f"Computer's choice: {computer_choice}\n"
                             f"Result: {result}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

for choice in CHOICES:
    tk.Button(button_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=20)
result_label.pack()

root.mainloop()