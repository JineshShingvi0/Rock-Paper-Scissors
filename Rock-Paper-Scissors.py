import random

choices = ["rock", "paper", "scissors"]
player_point=0
computer_point=0
count=5
while (count>0):
    computer = random.choice(choices)

    player = input("Enter Rock, Paper or Scissors: ").lower()

    if player not in choices:
        print("Invalid Choice!")
        continue

    print("Computer chose:", computer)

    if player == computer:
        print("It's a Draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 You Win!")
        player_point+=1
    else:
        print("😢 Computer Wins!")
        computer_point+=1
    print("Player points=",player_point)
    print("Computer Points=",computer_point)
         
    if(player_point == 3):
        print("🎉 You Win!")
        break
    if(computer_point == 3):
        print("😢 Computer Wins!")
        break

