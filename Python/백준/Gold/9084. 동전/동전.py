import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, input().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])
