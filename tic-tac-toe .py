def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(str(i))

    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X, 0 for O
    print("\n🎮 Welcome to TIC-TAC-TOE! 🎮\n")
    print("Instructions: Enter the number shown on the board to mark your move.\n")

    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("🔵 X's Turn")
            value = int(input("Enter your move (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("⚠️  Cell already occupied! Try again.")
                continue
        else:
            print("🟠 O's Turn")
            value = int(input("Enter your move (0-8): "))
            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
            else:
                print("⚠️  Cell already occupied! Try again.")
                continue

        winner = checkWin(xState, zState)
        if winner != -1:
            printBoard(xState, zState)
            if winner == 1:
                print("🏆 Congratulations! X wins the game!")
            else:
                print("🏆 Congratulations! O wins the game!")
            break

        if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
            printBoard(xState, zState)
            print("🤝 It's a DRAW!")
            break

        turn = 1 - turn  # Switch turn

   
