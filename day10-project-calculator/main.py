import calculator_art

print(calculator_art.logo)

def add(n1, n2):
   return n1+n2

def subtract(n1,n2):
   return n1-n2

def multiply(n1, n2):
   return n1*n2

def divide(n1,n2):
   return n1/n2

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

def calculator():
   
   num1 = float(input("what's the first number?: "))
   num2 = float(input("what's the second number?: "))
   
   # for key in operations.keys():
   #    print(key)
   
   for key in operations:
      print(key)
   
   operation_symbol = input("Pick an operation from the line above: ")
   
   function = operations[operation_symbol]
   res = function(num1, num2)
   
   print(f"{num1} {operation_symbol} {num2} = {res}")
   
   user_option = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculator.: ")
   while user_option == "y":
      num1 = res
      operation_symbol = input("Pick an operation: ")
      num2 = int(input("what's the next number?: "))
      function = operations[operation_symbol]
      res = function(num1,num2)
      print(f"{num1} {operation_symbol} {num2} = {res}")
      user_option = input(f"Type 'y' to continue calculating with {res}, or type 'n' to  start a new calculator.: ")

   if user_option == "n":
      calculator() # recursion



calculator()
