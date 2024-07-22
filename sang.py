import random
sum=0
count=0
while True:
    possible_actions = ["rock", "paper", "scissors"]
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        if user_action in possible_actions:
            break
        else:
            print("you should select (rock, paper, scissors)")


    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            sum+=1

        else:
            print("Paper covers rock! You lose.")
            count+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            sum+=1
        else:
            print("Scissors cuts paper! You lose.")
            count+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            sum+=1
        else:
            print("Rock smashes scissors! You lose.")
            count+=1
    if sum==3 or count==3:
        print("computer=",count,"\nyou=",sum)
        break
