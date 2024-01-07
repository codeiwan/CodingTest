import sys
input = sys.stdin.readline


def calculate(M, N, x, y):
    day = x
    while day <= M * N:
        if (day - x) % M == 0 and (day - y) % N == 0:
            return day
        day += M
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(calculate(M, N, x, y))