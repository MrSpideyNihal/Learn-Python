"""Play Rock Paper Scissors."""
import random

def get_computer_move():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

def game():
    """Play Rock Paper Scissors with computer."""
    user_move = input('Enter rock, paper or scissors: ').lower()
    comp_move = get_computer_move()
    if user_move == comp_move:
        return 'Tie'
    elif (user_move == 'rock' and comp_move == 'scissors') or
         (user_move == 'paper' and comp_move == 'rock') or
         (user_move == 'scissors' and comp_move == 'paper'):
        return 'You win'
    else:
        return 'Computer wins'

if __name__ == "__main__":
    print(game())
