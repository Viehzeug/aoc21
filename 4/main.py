import numpy as np

def read(lines):
    numbers = np.fromstring(lines[0], dtype=int, sep=',')
    boards = []

    pos = 2 
    while pos < len(lines):
        board = []
        for i in range(5):
            board.append(np.fromstring(lines[pos], dtype=int, sep=' '))
            pos += 1
        board = np.stack(board, axis=0)
        boards.append(board)
        pos += 1
    return numbers, boards

def update(n, board, marked):
    I = (board == n)
    return marked | I

def check(marked):
    return ((marked.sum(axis=0) == marked.shape[0]).any() or
            (marked.sum(axis=1) == marked.shape[1]).any())


def score(n, board, marked):
    return n * (board * (1-marked)).sum()

def play(numbers, boards):
    marked = [np.zeros(board.shape, dtype=np.bool) for board in boards]
    for i, n in enumerate(numbers):
        for j, board in enumerate(boards):
            if not check(marked[j]):
                marked[j] = update(n, boards[j], marked[j])
                if check(marked[j]):
                    s = score(n, boards[j], marked[j])
                    print(f"Board {j} won with score {s}")

with open('input.txt') as f:
    lines = f.readlines()
    numbers, boards = read(lines)
    play(numbers, boards)
