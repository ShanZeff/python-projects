import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won! :D"
    
    return "You lost! :<"

def is_win(player, oppponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and oppponent == 's') or (player == 's' and oppponent == 'p') \
        or (player == 'p' and oppponent == 'r'):
        return True

print(play())