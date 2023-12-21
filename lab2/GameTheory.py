import numpy as np
from operator import add, neg

payoff_matrix = np.array([[1, 7, 4,],
                           [8, 3, 9,],
                           [3, 1, 4,]])

def findMixedStrategies(payoff_matrix, iterations=1000000):
    transpose = list(zip(*payoff_matrix))
    # Определяем количество строк и столбцов в матрице выигрышей
    numrows = len(payoff_matrix)
    numcols = len(transpose)

    row_cum_payoff = [0] * numrows
    col_cum_payoff = [0] * numcols
    colpos = range(numcols)
    rowpos = map(neg, range(numrows))
    colcnt = [0] * numcols
    rowcnt = [0] * numrows
    active = 0
    for i in range(iterations):
        rowcnt[active] += 1
        col_cum_payoff = list(map(add, payoff_matrix[active], col_cum_payoff))
        active = -1
        min_col_cum_payoff = min(col_cum_payoff, default=None)
        if min_col_cum_payoff is not None:
            active = col_cum_payoff.index(min_col_cum_payoff)
        if active == -1:
            break
        colcnt[active] += 1
        row_cum_payoff = list(map(add, transpose[active], row_cum_payoff))
        active = -1
        max_row_cum_payoff = max(row_cum_payoff, default=None)
        if max_row_cum_payoff is not None:
            active = row_cum_payoff.index(max_row_cum_payoff)
        if active == -1:
            break
    value_of_game = (max(row_cum_payoff) + min(col_cum_payoff)) / 2.0 / iterations
    for i in range(len(rowcnt)):
        rowcnt[i] = rowcnt[i]/iterations
    for i in range(len(colcnt)):
        colcnt[i] = colcnt[i]/iterations
        
    return rowcnt, colcnt, value_of_game

print(findMixedStrategies(payoff_matrix))
