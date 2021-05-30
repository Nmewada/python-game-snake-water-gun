# Snake Water Gun or Rock Paper Scissors
import random

def gameWin(comp, you):
    if comp == you:  # Declare a tie!
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Computer Turn: Snake(s) Water(w) or Gun(g)?\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Player Turn: Snake(s) Water(w) or Gun(g)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"Player chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")