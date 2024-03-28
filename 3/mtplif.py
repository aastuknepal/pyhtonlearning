print("Welcome to the calculator")
name1= input("Enter your name")
name2= input("Enter the other name")

cs= name1 + name2
ls= cs.lower()
t = ls.count("t")
r = ls.count("r")
u = ls.count("u")
e = ls.count("e")

true= t + r + u + e

l = ls.count("l")
o = ls.count("o")
v = ls.count("v")
e= ls.count("e")

love = l + o + v + e
score = int(str(love) + str(true))


if (score < 10) or (score >90):
    print(f"your score is {score}, you go ahead")
elif (score >=40) and (score <=50):
    print(f"your score is {score}, you can be together")
else:
    print(f"your score is {score}, ok?")
        



