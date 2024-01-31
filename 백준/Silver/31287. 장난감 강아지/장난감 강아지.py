delta = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
N, K = map(int,input().split())
S = input()

xt, yt = 0, 0
for C in S:
    dx, dy = delta[C]
    xt, yt = xt + dx, yt + dy

x, y = 0, 0
for C in S:
    dx, dy = delta[C]
    x, y = x + dx, y + dy
    if (x == 0 if xt == 0 else (x % xt == 0 and -K+1 <= x // xt <= 0)):
        if (y == 0 if yt == 0 else (y % yt == 0 and -K+1 <= y//yt <= 0 and (xt == 0 or x//xt == y//yt))):
            print('YES')
            break
else:
    print('NO')