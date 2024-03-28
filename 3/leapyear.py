print("Checking if leap year or not")
year=int(input("Please enter year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("It is a leap year")
        else:
            print("It is not  a leap year")
    else:
        print(" leap year")
else:
    print("It is not a leap year")