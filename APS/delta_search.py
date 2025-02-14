# 델타 이용
# 주변 원소 탐색 -> 우하좌상, 대각선 모두 포함.
# 1. NxN
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

delta_1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
delta_2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

for i in range(N):
    for j in range(N):
        # 우하좌상
        for di, dj in delta_1:
            new_i = i + di
            new_j = j + dj
            if (0 <= new_i < N) and (0 <= new_j < N):
                print(arr[new_i][new_j], end=' ')

        # 대각선 우하, 좌하, 좌상, 우상
        for di, dj in delta_2:
            new_i = i + di
            new_j = j + dj
            if (0 <= new_i < N) and (0 <= new_j < N):
                print(arr[new_i][new_j], end=' ')

        print(arr[i][j])

# 2. NxM

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

delta_1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
delta_2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

for i in range(N):
    for j in range(M):
        # 우하좌상
        for di, dj in delta_1:
            new_i = i + di
            new_j = j + dj
            if (0 <= new_i < N) and (0 <= new_j < M):
                print(arr[new_i][new_j], end=' ')

        # 대각선 우하, 좌하, 좌상, 우상
        for di, dj in delta_2:
            new_i = i + di
            new_j = j + dj
            if (0 <= new_i < N) and (0 <= new_j < M):
                print(arr[new_i][new_j], end=' ')

        print(arr[i][j])