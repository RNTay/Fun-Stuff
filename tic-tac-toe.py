def game_over(g):
    """
    Our strategy:
    1. Check all rows.
        If there is a winner, return True
    2. Check all columns.
        If there is a winner, return True
    3. Check both diagonals: top-left to bottom-right; top-right to bottom-left.
        If there is a winner, return True.
    4. If we have found no winners, it means either:
        (a) the game is not yet over, return False,
        or
        (b) the game is a draw, return True.
    """
    # g = grid of the tic tac toe game
    length = len(g)  # side length of the board
    # We can simply set the length to 3 for a standard tic-tac-toe,
    # but this code allows for a tic-tac-toe of any size.

    # rows
    for row in g:
        # If L is a list and m is some object, then
        # L.count(m) will count the number of times m appears in L.
        if row.count(row[0]) == length:
            # If row[0] appears as many times as the length of the row,
            # then it must completely fill the row.
            if row[0] is not None:
                # Now we know row[0] is not an empty space,
                # so the whole row is not simply a boring [None, None, None].
                # This means we have a winner. It's either [1, 1, 1] or [0, 0, 0].
                print('Winner =', row[0])  # Print the winner.
                return True  # The game has ended, because there is a winner.

    # columns
    for column_index in range(length):
        # We can use list comprehension to get the columns of g.
        column = [row[column_index] for row in g]
        # For the above, if column_index is 1, then it will make the list
        # [g[0][1], g[1][1], g[2][1]]
        if column.count(column[0]) == length:
            if column[0] is not None:
                print('Winner =', column[0])
                return True

    # diagonals
    diagonal1 = [g[i][i] for i in range(length)]  # diagonal from top left to bottom right
    # The above uses list comprehension, and creates the diagonal
    # [g[0][0], g[1][1], g[2][2]].
    if diagonal1.count(diagonal1[0]) == length:
        if diagonal1[0] is not None:
            print('Winner =', diagonal1[0])
            return True
    diagonal2 = [g[i][(length-1) - i] for i in range(length)]  # diagonal from top right to bottom left
    # Similarly, the above creates the diagonal
    # [g[0][2], g[1][1], g[2][0]].
    if diagonal2.count(diagonal2[0]) == length:
        if diagonal2[0] is not None:
            print('Winner =', diagonal2[0])
            return True

    # We have found no completely filled row, column, or diagonal.
    # Let's check if the game is completely filled (and thus a draw),
    # or if there are still empty positions (i.e. our grid still has None).
    for row in g:
        for item in row:
            if item is None:
                # We have found an empty position. So the game is not over yet.
                print('There are still empty spaces.')
                return False
    # We have found no empty positions. So this must be a draw.
    print('This game is a draw.')
    return True


tic_tac_toe_1 = [[1, 0, None],
                 [1, 0, None],
                 [1, None, None]]
print(game_over(tic_tac_toe_1))

tic_tac_toe_2 = [[None, 0, 1],
                 [1, 0, 0],
                 [1, None, None]]
print(game_over(tic_tac_toe_2))


