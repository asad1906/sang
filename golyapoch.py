from random import randint,choice
me=0
computer=0
while(True):
    gol=choice(["left","right"])
    user=input("Enter left or right:").lower()
    if user==gol:
        print("you win !")
        me+=1
    else:
        print("you lose !")
        computer+=1
    if computer==5 or me==5:
        break
