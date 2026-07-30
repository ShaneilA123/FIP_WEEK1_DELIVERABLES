import random

q_table = {}


def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def check_tie(board):
    return " " not in board


def ai_move(board):
    empty = [i for i in range(9) if board[i] == " "]

    if random.random() < 0.2:
        return random.choice(empty)

    return max(empty, key=lambda x: q_table.get((tuple(board), x), 0))


def train_ai():
    for game in range(5000):
        board = [" "] * 9

        while True:
            state = tuple(board)
            move = ai_move(board)
            board[move] = "X"

            if check_winner(board, "X"):
                q_table[(state, move)] = 1
                break

            if check_tie(board):
                break

            empty = [i for i in range(9) if board[i] == " "]
            board[random.choice(empty)] = "O"

            if check_winner(board, "O"):
                q_table[(state, move)] = -1
                break


def main_game_loop():
    board = [" "] * 9

    while True:
        move = ai_move(board)
        board[move] = "X"

        print(board[0:3])
        print(board[3:6])
        print(board[6:9])

        if check_winner(board, "X"):
            print("AI wins!")
            break

        if check_tie(board):
            print("It's a tie!")
            break

        choice = int(input("Choose a position (1-9): ")) - 1

        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Position already taken!")
            continue

        if check_winner(board, "O"):
            print("You win!")
            break

        if check_tie(board):
            print("It's a tie!")
            break



train_ai()

main_game_loop()
