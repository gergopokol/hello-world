def play_game():
    board = create_board()
    while evaluate(board) == 0:
        board = random_place(board,1)
        if evaluate(board) != 0:
            break
        board = random_place(board,2)
    return evaluate(board)

play_game()
