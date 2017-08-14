def col_win(board, player):
    for col in range(2):
        if np.where(board[:,col] == player)[0].size == 3:
           return True
    return False


col_win(board, 1)

