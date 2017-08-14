def possibilities(board):
    poss_arr = np.where(board == 0)
    possibilities = []
    for i in range(poss_arr[0].size-1):
        possibilities += [(poss_arr[0][i],poss_arr[1][i])]
    return possibilities

possibilities(board)

