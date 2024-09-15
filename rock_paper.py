import random as rd
import tkinter as tk
from tkinter import messagebox 
# Function Declaration for Winner 
def get_winner(user, computer): #user: user choice, computer: computer Choice
    if user == computer:
        return "It's a Tie"
    elif (user == 'rock' and computer == 'scissors')or \
        (user == 'scissors' and computer == 'paper')or \
        (user == 'paper' and computer == 'rock'):
        return "You Win !!"
    else:
        return "You Lose !!"
# function for User choice
def play(user):
    global uscore, cscore #uscore: user score, cscore: computer score
    computer = rd.choice(["rock", "paper", "scissors"])
    res = get_winner(user, computer)
    if res == "You Win !!":
        uscore += 1
    elif res == "You Lose !!":
        cscore += 1
    # Since we are using user inteface we use labels in python
    result['text'] = f"Your Choice {user}, Computer Choice {computer}. {res}"
    score['text'] = f"Score: You {uscore} - {cscore} Computer"
# Function for reset the stats
def reset():
    global uscore, cscore
    uscore = 0
    cscore = 0
    result['text'] = "Make Your Move !"
    score['text'] = "Score : You 0 - 0 Computer"
#setting up the window
window = tk.Tk()
window.title("Rock Paper Scissor game by Sathvik")
window.geometry("600x600")
uscore = 0
cscore = 0
# creating labels
title = tk.Label(window, text = "Rock - Paper - Scissor Python Task CodSoft", font  = ("Algerian", 16))
title.pack(pady = 10)
instructions = tk.Label(window, text = "Choose ROck, Paper and Scissors")
instructions.pack()
result = tk.Label(window, text = "Make Your Move !!", font = ("Ebrima", 12))
result.pack(pady = 10)
score = tk.Label(window, text = "Score: You 0 - 0 Computer", font = ("Arial", 12))
score.pack(pady = 10)
#create the buttons for the rock, paper and scissors
rock = tk.Button(window, text = "Rock", width  = 20, command = lambda: play("rock"))
rock.pack(pady = 5)
paper = tk.Button(window, text = "Paper", width  = 20, command = lambda: play("Paper"))
paper.pack(pady = 5)
scissor = tk.Button(window, text = "Scissor", width  = 20, command = lambda: play("Scissor"))
scissor.pack(pady = 5)
# creating the reset buttom
reset = tk.Button(window, text = "Reset", width = 10, command = reset)
reset.pack(pady = 20)
# starting the Tkinter event Loop
window.mainloop()
