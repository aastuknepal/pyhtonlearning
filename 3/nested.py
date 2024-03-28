print("Please enter your height")
height= int(input("Enter here"))
if height >120:
    print("You are eligible")
    age = int(input("Please enter your age"))
    if age <12:
        print("pay $5")
    elif age <=18:
        print("Pay $7")
    else:
        print("pay 50$")
        
    
else:
    print("Sorry, you might have to increase your height")