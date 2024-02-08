N = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])

dp = [[[0]*61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1

comb = [(9,3,1), (9,1,3), (3,9,1), (3,1,9), (1,9,3), (1,3,9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for c in comb:
                    I = i-c[0] if i-c[0] >= 0 else 0
                    J = j-c[1] if j-c[1] >= 0 else 0
                    K = k-c[2] if k-c[2] >= 0 else 0
                    if dp[I][J][K] == 0 or dp[I][J][K] > dp[i][j][k] + 1:
                        dp[I][J][K] = dp[i][j][k] + 1

print(dp[0][0][0]-1)
