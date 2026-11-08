board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
valid = True
for i in range(9):
    row = [x for x in board[i] if x != "."]
    col = [board[r][i] for r in range(9) if board[r][i] != "."]
    if len(row) != len(set(row)) or len(col) != len(set(col)):
        valid = False
for box_r in range(0, 9, 3):
    for box_c in range(0, 9, 3):
        box = []
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if board[r][c] != ".":
                    box.append(board[r][c])
        if len(box) != len(set(box)):
            valid = False
print(valid)