from collections import deque

def process_list(lst):
    ans = deque()
    num = 0

    for val in reversed(lst):
        num += 1
        if val == 1:
            ans.appendleft(num)
        elif val == 2:
            ans.insert(1, num)
        elif val == 3:
            ans.append(num)

    return ans

def main():
    N = int(input())
    lst = list(map(int, input().split()))
    result = process_list(lst)
    print(*result)

if __name__ == "__main__":
    main()