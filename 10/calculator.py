def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2



operations = {"+" : add,
              "-" : subtraction,
              "*" : multiply,
              "/" : divide
              }

num1 = int(input("What is the first numbr"))
num2 = int(input("What is the second numbere"))

for symbol in operations:
    print(symbol)
    
operation_symbol = input("Pick an operation from the list above")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1}  {operation_symbol}  {num2}  = {answer}")
