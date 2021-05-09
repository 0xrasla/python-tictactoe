#GLOBALS

board = ['_','_','_','_','_','_','_','_','_']

player = "X"

winner = ""

game_over = False


def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_for_winner(board, game_over, winner, player):
    if board[1] == board[2] == board[0] and board[0] != "_":
        game_over, winner = True, player
    if board[4] == board[5] == board[3] and  board[3] != "_":
        game_over, winner = True, player
    if board[7] == board[8] == board[6] and board[7] != "_":
        game_over, winner = True, player
    if board[4] == board[8] == board[0] and board[4] != "_":
        game_over, winner = True, player
    if board[4] == board[6] == board[2] and board[4] != "_":
        game_over, winner = True, player
    if board[3] == board[6] == board[0] and board[3] != "_":
        game_over, winner = True, player
    if board[4] == board[7] == board[1] and board[4] != "_":
        game_over, winner = True, player
    if board[5] == board[8] == board[2] and board[5] != "_":
        game_over, winner = True, player

    return game_over, winner

def user_input(pos, board, player):
    board[int(pos) - 1] = player

def switch_player(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

    return player

if __name__ == '__main__':
    print_board(board)
    while not game_over:
        print()
        pos = input(player + ' turn ')
        posible_inputs = ['1','2','3','4','5','6','7','8','9']
        while pos not in posible_inputs or board[int(pos) - 1] != "_":
            pos = input(player + ' turn ')
        user_input(pos, board, player)
        game_over, winner_name = check_for_winner(board, game_over, winner, player)
        if "_" not in board and game_over == False:
            print("game over! No one Win")
            break
        print()
        if winner_name != "":
            print("The Winner is ", player)

        print_board(board)
        player = switch_player(player)