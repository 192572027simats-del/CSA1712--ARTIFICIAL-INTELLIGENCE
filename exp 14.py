
def alphabeta(board, alpha, beta, is_max):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return 1 if board[a] == 'X' else -1

    if ' ' not in board:
        return 0

    if is_max:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, alphabeta(board, alpha, beta, False))
                board[i] = ' '
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, alphabeta(board, alpha, beta, True))
                board[i] = ' '
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

board = [' '] * 9

best_score = -float('inf')
best_move = -1

for i in range(9):
    board[i] = 'X'
    score = alphabeta(board, -float('inf'), float('inf'), False)
    board[i] = ' '

    if score > best_score:
        best_score = score
        best_move = i

print("Best move for X:", best_move + 1)
print("Score:", best_score)
