print("Treasure Island")
print("Your objective is to find the treasure under the sea")

# this back slas enables us to use the quote in the middle

choice1= input('you\'re on a crossroad, where do you want to go? Type "left" or "right"').lower()

if choice1 == "left":
    choice2=input("You ara now in the middle of an island and npw type wait to wait for the boat or type swim to swim through the lake").lower()
    if choice2 == "wait":
        #game will continue
        choice3= input("YOu are now safe now choose the door type red or yellow or blue").lower()
        if choice3 == "red":
            print("congratulation you won")
        elif choice3== "blue":
            print("There is full of angry lions and they ate you you loose")
        elif choice3 == "yellow":
            print("You chose the door where there is lava burining so you lose")
        else:
            print("you chose the door that does not even exists so you loose")
        
    else:
        print("you got attacked by the fish game over")
    
    
    
else:
        print("You fell into the hole game over")

