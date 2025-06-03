from random import randint


print("Welcome to the TicTacToe game!");

userFigureChoice = input('Do you want to be X or O: ');
userChoice = ''


grids = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


def createBoard():
    print(f"  {grids[0]} | {grids[1]} | {grids[2]}")
    print("  --+---+---")
    print(f"  {grids[3]} | {grids[4]} | {grids[5]}")
    print("  --+---+---")
    print(f"  {grids[6]} | {grids[7]} | {grids[8]}")

    
def get_userChoice():
        while True:
             userChoice = int(input("Choose a square from 1-9: "))
             if(grids[userChoice-1].lower() == 'x' or grids[userChoice-1].lower() == "o"):
                 userChoice = int(input("Choose another square!"));
                 continue;
             else:
                grids[userChoice-1] = userFigureChoice;
                break;
    

      





def get_computerChoice():
    computerChoice = 'O' if userFigureChoice.lower() == 'x' else 'X'
    
    while True:
        index = randint(0,8)
        if grids[index].lower() not in ['x', 'o']:
            grids[index] = computerChoice
            break
        else:
            print("Computer picked a taken spot, retrying...")

        

def play():
    if(userFigureChoice.lower() == 'x'):
        while True:
            createBoard();
            get_userChoice();
            get_computerChoice()
    else:
        while True:
            createBoard()
            get_computerChoice();
            get_userChoice();

play();