import random
print("This is the lottery program that chose the randpm name")

names= input("Enter your names separated by commas")

nam= names.split(", ")

# x= len(nam)

# random= random.randint(0,x-1)

# print(random)
# person= nam[random]
person= random.choice(nam)
print(person + "is gonna pay the bill")
  


