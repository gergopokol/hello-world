def row_win(board, player):
    for row in range(2):
        if np.where(board[row,:] == player)[0].size == 3:
           return True
    return False


row_win(board, 1)

