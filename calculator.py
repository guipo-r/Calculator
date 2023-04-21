from replit import clear

from art import logo


#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#Substract

def substract(n1, n2):
  return n1 - n2

#Multiply

def multiply(n1, n2):
  return n1 * n2

#Divide

def divide(n1,n2):
  return n1 / n2

#Power

def power(n1,n2):
  return n1 ** n2

#Modulus

def modulus(n1, n2):
  return n1 % n2


#Create dictionary with all functions
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
  "**": power,
  "%": modulus
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    chosen_op = operations[operation_symbol]
    answer = chosen_op(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    
    ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart.: ")
    if ask == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
