#rock_paper_scissor
import random
def play():
    user=input(["'r':rock, 'p':paper, 's':scissor"])
    comp=random.choice(['r','p','s'])
    if user == comp:
        return 'Its a tie'
    elif win(user,comp):
        return 'you won'
    return 'you lost'
def win(player,comp):
    if player == 'r' and comp == 's'  or player == 's' and comp == 'p' or player =='p' and comp =='r':
        return True
print(play())