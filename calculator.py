def add(n1, n2):
    return n1 + n2
#write down other functions
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
#specify keys and store them as values in dictionary  key:value
keys={"+":add,       #storing function so can't use parenthesis () to trigger or store as string""
      "-":subtract,
      "*":multiply,
      "/":divide
      }


#print(keys["*"](4,2)) #call the dictionary by specifying key not index and then add inputs as it retraces the function

def calculator():
    should_continue=True
    number1=int(input("Enter your first number: "))
    while should_continue:
        for symbol in keys:
            print(symbol)
        operator = input("Enter your operator: ")
        number2=int(input("Enter your second number: "))
        answer= keys[operator](number1,number2)
        print(f'the answer is {answer}')
        choice=input(f"type 'y' to continue with {answer} and 'n' to start new calculation:")
        if choice=='y':
            number1=answer
        else:
            should_continue=False
            print("\n"*100)
            calculator()

calculator()

# if operator=="+":
#     result=add(number1,number2)
# elif operator=="-":
#     result=subtract(number1,number2)
# elif operator=="*":
#     result=multiply(number1,number2)
# elif operator=="/":
#     result=divide(number1,number2)
# print(result)
