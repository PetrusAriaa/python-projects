from random import randint

def roll():
    roll =  randint(1,1000)
    if roll % 3 == 1:
        return "rock"
    elif roll % 3 == 2:
        return "paper"
    else:
        return "scissors"

input("FIRST PLAYER ROLL! [press enter]")
rolling1 = roll()
print(rolling1)
input("SECOND PLAYER ROLL! [press enter]")
rolling2 = roll()
print(rolling2)

if rolling1 == "rock":
    if rolling2 == "rock":
        print("DRAW!")
    elif rolling2 == "paper":
        print("PLAYER 2 WINS!")
    else:
        print("PLAYER 1 WINS!")
elif rolling1 == "paper":
    if rolling2 == "paper":
        print("DRAW")
    elif rolling2 == "scissors":
        print("PLAYER 2 WINS!")
    else:
        print("PLAYER 1 WINS!")
else:
    if rolling2 == "scissors":
        print("DRAW!")
    elif rolling2 == "rock":
        print("PLAYER 2 WINS!")
    else:
        print("PLAYER 1 WINS!")




