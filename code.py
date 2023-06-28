choose = input("choose ur call:")

import random
computer_choice = random.choice(["rock" , "paper" , "scissor"])

print(f"computer choice is: {computer_choice}")

if (choose == "rock") and (computer_choice == "scissor"):
    print("you won")

elif (choose == "paper")  and (computer_choice == "rock"):
    print("you won")

elif(choose == "scissor") and (computer_choice == "paper"):
    print("you won")

elif (choose == "rock") and (computer_choice == "rock"):
    print("match tie")

elif (choose == "paper")  and (computer_choice == "paper"):
    print("match tie")

elif(choose == "scissor") and (computer_choice == "scissor"):
    print("match tie")
else:
    print("computer won")
