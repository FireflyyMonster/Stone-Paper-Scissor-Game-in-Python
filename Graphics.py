import tkinter as tk
from tkinter import messagebox
import random


# Game Logic
def game(computer, you):
    if computer == you:
        return "It's a tie!"
    elif computer == "r":
        return "You Won!" if you == "p" else "You Lost!"
    elif computer == "p":
        return "You Won!" if you == "s" else "You Lost!"
    elif computer == "s":
        return "You Won!" if you == "r" else "You Lost!"


# Event Handler for User Selection
def on_choice(user_choice):
    global rounds_played

    if rounds_played < 6:
        choices = ["r", "p", "s"]
        computer_choice = random.choice(choices)

        result = game(computer_choice, user_choice)

        user_choice_text = choice_map[user_choice]
        computer_choice_text = choice_map[computer_choice]

        result_text.set(f"You chose: {user_choice_text}\nComputer chose: {computer_choice_text}\n{result}")

        if "You Won!" in result:
            your_marks.append(1)

        rounds_played += 1

        if rounds_played == 6:
            final_score = sum(your_marks)
            messagebox.showinfo("Game Over",
                                f"Your total score is {final_score}\nYour 5 chances have ended, Thanks for Playing!")
            root.destroy()


# Initialize GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

choice_map = {'r': "Rock", 'p': "Paper", 's': "Scissors"}

your_marks = []
rounds_played = 0
result_text = tk.StringVar()
result_text.set("Welcome to Rock, Paper, Scissors!\nChoose your weapon:")

# Create Widgets
label = tk.Label(root, textvariable=result_text, font=('Helvetica', 14), justify='center')
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: on_choice('r'))
paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: on_choice('p'))
scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: on_choice('s'))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
