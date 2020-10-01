import random


def display_board(board):
    print("\n" * 100)
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])


def player_input():
    while True:
        marker = input("Player 1: Choose X or O: ").upper()
        if marker == 'X' or marker == 'O':
            break

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(position, board, marker):
    board[position-1] = marker


def board_is_full(board):
    if board.count(' ') < 1:
        return True
    else:
        return False


def winning_player(board, mark):
    response = False
    positions = []
    if board.count(mark) < 3:
        return response
    if board[1] == board[2] == board[3] == mark:
        response = True
    elif board[4] == board[5] == board[6] == mark:
        response = True
    elif board[7] == board[8] == board[9] == mark:
        response = True
    elif board[1] == board[4] == board[7] == mark:
        response = True
    elif board[2] == board[5] == board[8] == mark:
        response = True
    elif board[3] == board[6] == board[9] == mark:
        response = True
    elif board[1] == board[5] == board[9] == mark:
        response = True
    elif board[3] == board[5] == board[7] == mark:
        response = True

    return response


def space_check(board, position1):
    return board[position1] == ' '


def player_choice(board):
    position = 0 

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


print("Welcome to TIC TAC TOE")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(position, theBoard, player1_marker)

            if winning_player(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if board_is_full(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(position, theBoard, player2_marker)

            if winning_player(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if board_is_full(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
