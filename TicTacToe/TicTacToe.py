from random import randint


print("Welcome to the TicTacToe game!");

userFigureChoice = input('Do you want to be X or O: ');
userChoice = ''


grids = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


def createBoard(grids):
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

def checkWin(symbol):
    if grids[0].lower() == symbol and grids[1].lower() == symbol and grids[2].lower() == symbol:
        return True
    elif grids[3].lower() == symbol and grids[4].lower() == symbol and grids[5].lower() == symbol:
        return True
    elif grids[6].lower() == symbol and grids[7].lower() == symbol and grids[8].lower() == symbol:
        return True
    elif grids[0].lower() == symbol and grids[3].lower() == symbol and grids[6].lower() == symbol:
        return True
    elif grids[1].lower() == symbol and grids[4].lower() == symbol and grids[7].lower() == symbol:
        return True
    elif grids[2].lower() == symbol and grids[5].lower() == symbol and grids[8].lower() == symbol:
        return True
    elif grids[0].lower() == symbol and grids[4].lower() == symbol and grids[8].lower() == symbol:
        return True
    elif grids[2].lower() == symbol and grids[4].lower() == symbol and grids[6].lower() == symbol:
        return True
    return False




def play():
    while True:
        computerCount = 0
        userCount = 0
        global grids

        if userFigureChoice.lower() == 'x':
            while True:
                createBoard(grids)
                result = checkWin(userFigureChoice.lower())
                if result:
                    print(result)
                    userCount += 1
                    print(f'Congratulations User won!: {userCount}')
                    break

                get_userChoice()
                result = checkWin(userFigureChoice.lower())
                if result:
                    createBoard(grids)
                    userCount += 1
                    print(f'Congratulations User won!: {userCount}')
                    break

                get_computerChoice()
                result = checkWin('o' if userFigureChoice.lower() == 'x' else 'x')
                if result:
                    createBoard(grids)
                    computerCount += 1
                    print(f'Congratulations Computer won!: {computerCount}')
                    break
        else:
            while True:
                createBoard(grids)
                get_computerChoice()
                result = checkWin('o' if userFigureChoice.lower() == 'x' else 'x')
                if result:
                    createBoard(grids)
                    computerCount += 1
                    print(f'Congratulations Computer won!: {computerCount}')
                    break

                get_userChoice()
                result = checkWin(userFigureChoice.lower())
                if result:
                    createBoard(grids)
                    userCount += 1
                    print(f'Congratulations User won!: {userCount}')
                    break


        game = input("Do you wanna play again (yes/no)!").lower()
        if game != 'yes':
                print("Thanks for playing!")
                break
        else:
                grids = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                print("Starting a new game!")
        

        

play();