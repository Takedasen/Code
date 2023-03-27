import random

def get_choices():
    player_choice = input("Choose! Rock, Paper or Scissors: ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}    
    return choices

def check_win(player, computer):
    print (f"You Chose {player}, Computer chose: {computer}")
    if player == computer:
        return "ITS A DRAW!"

check_win("Rock", "Paper")