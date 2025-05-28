from random import randint

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']

while True:

    Password=""
    password_length = int(input("How long do you want you password to be"))

    while password_length>=100:
        if password_length >= 100:
            print("Give shorter length")
            password_length = int(input("How long do you want you password to be"))

    for x in range(password_length):
        list_Choice = randint(1,3)
        if list_Choice == 1:
            letter = randint(0, len(letterList) - 1)
            Password += letterList[letter]
        elif list_Choice == 2:
            number = randint(0, len(numberList) - 1)
            Password = Password+ numberList[number]
        elif list_Choice == 3:
            symbol = randint(0, len(symbolList) - 1)
            Password += symbolList[symbol]

    print(f'Your random generated password is {Password}')

    another= input("Do you want another password? (yes/no)").strip().lower()
    if another != "yes":
        print("Thank you for using this Password Generator!!")
        break
