print("Welcome to BMI advance")
height= float(input("Enter yout height"))
weight= float(input("Enter your weight"))
bmi= round(weight / height ** 2)
if bmi < 18:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, and you are normal weight")
elif bmi < 40:
    print(f"yoour bmi is {bmi}, you are overweight")
else: 
    print("You are obese")
    