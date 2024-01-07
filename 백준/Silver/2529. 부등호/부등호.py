def find(nums, iter):
    global found
    if found:
        return

    if len(res) > 1:
        if lst[len(res) - 2] == '<' and res[-2] > res[-1]:
            return
        elif lst[len(res) - 2] == '>' and res[-2] < res[-1]:
            return

    if iter == N+1:
        found = True
        return print(''.join(map(str, res)))

    for i in range(N+1):
        if not bit[i]:
            bit[i] = 1
            res.append(nums[i])
            find(nums, iter+1)
            bit[i] = 0
            res.pop()


N = int(input())
lst = list(input().split())

Max = [9-i for i in range(N+1)]
Min = [i for i in range(N+1)]

bit = [0] * (N+1)
res = []

found = False
find(Max, 0)

found = False
find(Min, 0)