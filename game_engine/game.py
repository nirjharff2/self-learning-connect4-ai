from board import Board

def play_game():
    board = Board()
    game_over = False
    turn = 0

    print()
    print("     === CONNECT 4 ===")
    board.print_board()

    while not game_over:
        col = int(input(f"Player {turn+1}, choose a column (0-6): "))
        if board.is_valid_location(col):
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, turn + 1)
            board.print_board()

            if board.winning_move(turn + 1):
                print(f"Player {turn+1} wins!")
                game_over = True

            turn = (turn + 1) % 2
        else:
            print("Column full! Choose another.")


play_game()
