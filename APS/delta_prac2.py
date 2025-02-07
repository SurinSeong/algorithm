# 5 x 5
# 각 요소와 이웃한 요소와의 차의 절댓값의 합은?

N = 5

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

all_total = 0
for i in range(N):
    for j in range(N):
        total = 0
        for di, dj in delta:
            new_i = i + di
            new_j = j + dj
            if (0 <= new_i < N) and (0 <= new_j < N):
                total += abs(arr[i][j] - arr[new_i][new_j])

        all_total += total

print(all_total)