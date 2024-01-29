result = -1
R = 0
C = 0
for r in range(9):
    row = list(map(int, input().split()))
    for c in range(9):
        if result < row[c]:
            result = row[c]
            R, C = r, c

print(result)
print(R+1, C+1)