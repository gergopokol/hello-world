def random_place(board, player):
    selection = possibilities(board)
    choice = random.choice(selection)
    return place(board, player, choice)

board = random_place(board, 2)
