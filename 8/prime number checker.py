print("Welcome to prime number checker")
def prime_checker(number):
    isprime = True
    for i in range(2, number):
        if number % i == 0:
            isprime = False
    if isprime:
        print("It is a prime number")
    else:
        print("It is not a prime number")       
            
    
prime_checker(13)
