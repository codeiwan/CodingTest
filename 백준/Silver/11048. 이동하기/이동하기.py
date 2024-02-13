import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]
dp[0][0] = arr[0][0]

for r in range(N):
    for c in range(M):
        if r < N-1:
            dp[r+1][c] = max(dp[r+1][c], dp[r][c] + arr[r+1][c])
        if c < M-1:
            dp[r][c+1] = max(dp[r][c+1], dp[r][c] + arr[r][c+1])


print(dp[N-1][M-1])