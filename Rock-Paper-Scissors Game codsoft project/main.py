import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Define game variables
user_score = 0
computer_score = 0

# Function to start a new round
def play_round():
    global user_score, computer_score
    user_choice = user_choice_var.get()
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner based on the game logic
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update the labels to display the user's and computer's choices and the result
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")

# Create labels and options
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instruction_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set("Rock")  # Default choice
user_choice_options = ["Rock", "Paper", "Scissors"]
user_choice_menu = tk.OptionMenu(root, user_choice_var, *user_choice_options)
user_choice_menu.pack()

play_button = tk.Button(root, text="Play", command=play_round)
play_button.pack()

user_choice_label = tk.Label(root, text="")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text="")
score_label.pack()

# Function to reset the scores and start a new game
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")

new_game_button = tk.Button(root, text="New Game", command=reset_scores)
new_game_button.pack()

# Run the application
root.mainloop()


