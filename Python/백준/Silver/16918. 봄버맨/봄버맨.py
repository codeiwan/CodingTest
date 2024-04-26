import sys
input = sys.stdin.readline
from collections import deque

q = deque()

R, C, N = map(int,input().rstrip().split())
board = [list(input().strip()) for _ in range(R)]


def bfs(q):
    while q:
        r, c = q.popleft()
        board[r][c] = '.'
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr <R and 0 <= nc <C and board[nr][nc] == 'O':
                board[nr][nc] = '.'


def simulate(t):
    global q, board
    if t == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    elif t % 2 == 1:
        bfs(q)
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    else:
        board = [['O'] * C for _ in range(R)]


for i in range(1, N+1):
    simulate(i)

for i in board:
    print(''.join(i))