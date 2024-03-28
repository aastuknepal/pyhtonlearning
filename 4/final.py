import random
user= int(input("what do you want? 1 for rock, 3 for scissor, and 2 for paper"))
computer= random.randint(0,3)
print(f"computer chose {computer}")

if user == 0 and computer ==2:
    print("you win")
elif computer > user:
    print("You loosr")
elif computer == user:
    print("Draw")
elif computer == 0 and user ==2:
    print("you lose")
     
else:
    print("You typed invalid number you lose")