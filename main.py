def print_board(board):
    print()
    for row in range(3):
        print(f" {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} ")
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(cell in ["X", "O"] for cell in board):
        return "Viik"

    return None


def player_move(board):
    while True:
        try:
            move = int(input("Vali koht (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Vali number 1 kuni 9.")
            elif board[move] in ["X", "O"]:
                print("See koht on juba hõivatud.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Palun sisesta number 1 kuni 9.")


def computer_move(board):
    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = "O"
            break


def main():
    board = [str(i) for i in range(1, 10)]

    print("Trips-traps-trull")
    print("Sina oled X ja arvuti on O.")
    
    while True:
        print_board(board)

        player_move(board)

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Viik":
                print("Mäng jäi viiki!")
            else:
                print(f"{result} võitis!")
            break

        computer_move(board)

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Viik":
                print("Mäng jäi viiki!")
            else:
                print(f"{result} võitis!")
            break


if __name__ == "__main__":
    main()