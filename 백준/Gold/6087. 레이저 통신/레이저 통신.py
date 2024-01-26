import sys
import heapq
input = sys.stdin.readline

def updateCntMaps(cnt, y, x):
    for i in range(4):
        dirY, dirX = dir[i]
        curY, curX = y, x
        while True:
            nextY, nextX = curY + dirY, curX + dirX
            if 0 <= nextY < h and 0 <= nextX < w:
                match arr[nextY][nextX]:
                    case '.':
                        if cntMaps[nextY][nextX] > cnt or (cntMaps[nextY][nextX] == cnt and chkMaps[i % 2][nextY][nextX] == False):
                            cntMaps[nextY][nextX] = cnt
                            chkMaps[i % 2][nextY][nextX] = True
                            heapq.heappush(hq, (cnt, nextY, nextX))
                            curY, curX = nextY, nextX
                        else:
                            break
                    case '*':
                        break
                    case 'C':
                        print(cnt)
                        exit(0)
            else:
                break


w, h = map(int, input().split())
arr = [list(input().strip()) for _ in range(h)]
cntMaps = [[sys.maxsize] * w for _ in range(h)]
chkMaps = [[[False] * w for _ in range(h)] for _ in range(2)]
hq = []
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            heapq.heappush(hq, (-1, i, j))
            arr[i][j] = '*'

            while hq:
                cnt, y, x = heapq.heappop(hq)
                updateCntMaps(cnt + 1, y, x)