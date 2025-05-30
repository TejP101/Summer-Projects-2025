from random import randint


print("Welcome to Rock Paper Scissor")

choices=["rock", "paper", "scissors"]

def get_user_choice():
    user_choice= input("Choose your weapon!").lower()
    while user_choice not in choices:
        print("Invalid Choice!")
        user_choice = input("Choose another weapon").lower()
    return user_choice



def get_computer_choice():
    return choices[randint(0,2)]

def winner(user,computer):
    if user == computer:
        return "Its a tie!"
    elif user == "rock" and computer == "scissors":
        return "User Wins!"
    elif user == "scissors" and computer == "paper":
        return "User Wins!"
    elif user == "paper" and computer == "rock":
        return "User Wins!"
    else:
        return "Computer Wins!"
    
def play():
    while True:

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f'The user chose {user_choice} and the computer chose {computer_choice}' )
        print(winner("rock","paper"))

        answer= input("Do you wanna play again yes or no?").lower()
        if answer != "yes":
            print("Thank you for playing!")
        
            break
play()





    


    


