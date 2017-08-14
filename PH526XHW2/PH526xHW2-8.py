def diag_win(board, player):
    if board[0,0] == player & board[1,1] == player & board[2,2] == player:
        return True
    if board[0,2] == player & board[1,1] == player & board[2,0] == player:
        return True
    return False


diag_win(board, 1)
