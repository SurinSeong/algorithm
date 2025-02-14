# 짝 홀 나눠서 생각해야 함.
# 5 x 5 일 때
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

N = 5

total = 0

for i in range(N):
    for j in range(N):
        if i == j:
            total += arr[i][j]
        elif i == (N - 1 - j):
            total += arr[i][j]

print(total)


# 4 x 4 일 때