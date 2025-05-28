isStillworking = True
print("Welcome to this CLI CAlC!!")
while isStillworking == True:
    firstNum= input("Enter your first number!")
    secNum= input("Enter your second number!")
    operator=input("What operator do you wanna use!")
    if operator=="+":
        result = float(firstNum) + float(secNum)
        print("------------------------------------------------------")
        print(f'The result of {firstNum} + {secNum} is {result}')
    elif operator == "-":
        result = float(firstNum) - float(secNum)
        print("------------------------------------------------------")
        print(f'The result of {firstNum} - {secNum} is {result}')
    elif operator == "*":
        result = float(firstNum) * float(secNum)
        print("------------------------------------------------------")
        print(f'The result of {firstNum} * {secNum} is {result}')

    elif operator == "/":
        result = float(firstNum) / float(secNum)
        print("------------------------------------------------------")
        print(f'The result of {firstNum} / {secNum} is {result}')
    else:
        result = float(firstNum) ** float(secNum)
        print("------------------------------------------------------")
        print(f'The result of {firstNum} ** {secNum} is {result}')
    

    print("Do you wanna keep going (yes/no)")
    if input().lower() != "yes":
        isStillworking= False
        print("Thanks for using the CLI Calculor!!")





    
