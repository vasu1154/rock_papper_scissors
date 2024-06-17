import random
def game():
    user=input("Choice 1 option 'r' for Rock ,'p' for Papper,'s' for Scissors : ")
    computer=random.choice(['r','p','s'])
    
    if user!='r'or'R'or 'p' or 'P' or 's' or 'S':
        return 'Invalid input'
    
    if user==computer:
        return 'It\'s a tie'
    if win(user,computer):
        return 'You Win!'
    
    return 'You Lost!'
        
    
def win(pl,opp):
    if(pl=='r' and opp=='s')or (pl=='s'and opp=='p')or(pl=='p'and opp=='r'):
        return True
print(game())