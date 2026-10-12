
def minimax(board, is_max):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return 1 if board[a] == 'X' else -1

    if ' ' not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_max else 'O'
            scores.append(minimax(board, not is_max))
            board[i] = ' '

    return max(scores) if is_max else min(scores)

board = [' '] * 9
player = 'X'

for turn in range(9):
    if player == 'X':
        best, move = -float('inf'), -1
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                if score > best:
                    best, move = score, i
        board[move] = 'X'
    else:
        move = int(input("Enter position (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move!")
            continue
        board[move] = 'O'

    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        print("-----")

    if minimax(board, True) == 1 or minimax(board, False) == -1:
        print("Game over!")
        break

    player = 'O' if player == 'X' else 'X'
