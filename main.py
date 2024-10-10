import random
import matplotlib.pyplot as plt


def cowsnbulls():
    target = str(random.randrange(0, 9999)).zfill(4)
    print(target)
    cow = bull = 0
    guess = str(input("Guess a number from 0 to 9999: ")).zfill(4)

    while cow != 4:
        for i in range(4):
            if target[i] == guess[i]:
                cow += 1
            else:
                bull += 1

        if cow == 4:
            break
        else:
            print(f"you got {cow} cows and {bull} bulls, try again")
            cow = bull = 0
            guess = str(input("Guess a number: ")).zfill(4)

    print("You guessed it!")


def birthplot():
    while True:
        maxday = int(input("What is the maximum number of birthdays for a month: "))
        if maxday > 0:
            break
        else:
            print("please select a valid number that's greater than 0")

    # initialize birthday array
    birthday = [0]*12
    for i in range(0, 12):
        birthday[i] = random.randrange(0, maxday)

    # create bar plot
    plt.bar(list(range(1, 13)), birthday)
    plt.xticks(list(range(1, 13)))
    plt.xlabel("month")
    plt.ylabel("number of days")
    plt.title("number of birthdays in each month")
    plt.show()


def morse():
    morsedic = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ' ': '   '}

    txt = input("Enter your text message:\n").upper()
    ciper = ""

    for i in txt:
        if i in morsedic.keys():
            if i == " ":
                ciper += morsedic[i]
            else:
                ciper = ciper + morsedic[i] + " "

    print(ciper)


def get_position(pr, posli, bd):
    if pr == 1:
        position = input("Player X, choose a position: ").upper()
    else:
        position = input("Player O, choose a position: ").upper()

    while True:
        if position in posli and bd[poslist.index(position)] == 0:
            return poslist.index(position)
        elif position not in posli:
            position = input("Incorrect input, choose a position: ").upper()
        else:
            idx = poslist.index(position)
            if bd[idx] != 0:
                position = input("Position already taken, choose a position: ").upper()


def print_board(bd):
    for i in range(9):
        print(str(bd[i]).replace("-1", "O").replace("1", "X"), end=" ")
        if (i+1) % 3 == 0:
            print()


def check_result(bd):
    # check rows
    for i in range(0, 9, 3):
        total = bd[i]+bd[i+1]+bd[i+2]
        if total == 3:
            return "player X wins"
        elif total == -3:
            return "player O wins"

    # check columns
    for i in range(3):
        total = bd[i]+bd[i+3]+bd[i+6]
        if total == 3:
            return "player X wins"
        elif total == -3:
            return "player O wins"

    # check diagnoal
    total = bd[0]+bd[4]+bd[8]
    if total == 3:
        return "player X wins"
    elif total == -3:
        return "player O wins"
    total = bd[2]+bd[4]+bd[6]
    if total == 3:
        return "player X wins"
    elif total == -3:
        return "player O wins"

    # check empty slots
    if 0 not in bd:
        return "tie"

    return None


def tictactoe():
    board = [0]*9
    print_board(board)
    poslist = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
    result = None
    player = 1  # player 1-X: 1 player 2-O: -1

    while result is None:
        pos_idx = get_position(player, poslist, board)
        if player == 1:
            board[pos_idx] = 1
            player = 2
        else:
            board[pos_idx] = -1
            player = 1

        result = check_result(board)
        print_board(board)

    print(f"\nGame over: {result}")


if __name__ == '__main__':
    game = input("Select a game:\n 1 - cowsNbulls\n "
                 "2 - birthdayPlot\n "
                 "3 - morseCode\n "
                 "4 - tictactoe\n")

    match game:
        case "1":
            cowsnbulls()
        case "2":
            birthplot()
        case "3":
            morse()
        case "4":
            tictactoe()
