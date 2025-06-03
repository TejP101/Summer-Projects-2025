print("Welcome to Tic Tac Toe!")

userChoice= input("Do you wanna be player O or player X?").lower()

s1="1"
s2="2"
s3="3"
s4="4"
s5="5"
s6="6"
s7="7"
s8="8"
s9="9"

row1= [s1, s2,s3]
row2=[s4,s5,s6]
row3=[s7,s8,s9]

def board():
    print(f"A  {s1} | {s2} | {s3}")
    print("  ---+---+---")
    print(f"B  {s4} | {s5} | {s6}")
    print("  ---+---+---")
    print(f"C  {s7} | {s8} | {s9}")


board()
