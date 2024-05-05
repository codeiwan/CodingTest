def check(num):
    length = len(num)
    for idx in range(1, length // 2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    return True


def solution(num):
    global N, res
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            solution(num + str(i))


N = int(input())
solution('1')