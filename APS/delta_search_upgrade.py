# N x N 배열에서 각 원소를 중심으로, 상하좌우/대각선의 k칸의 합계 중 최댓값은?
N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

delta_1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
delta_2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

for i in range(N):
    for j in range(N):
        # k칸의 합계
        total_k = 0
        for k in range(1, K+1):
            # 우하좌상
            for di, dj in delta_1:
                new_i = i + di*k
                new_j = j + dj*k
                if (0 <= new_i < N) and (0 <= new_j < N):
                    total_k += arr[new_i][new_j]
                    print(arr[new_i][new_j], end='|')

            # 대각선 우하, 좌하, 좌상, 우상
            for di, dj in delta_2:
                new_i = i + di*k
                new_j = j + dj*k
                if (0 <= new_i < N) and (0 <= new_j < N):
                    total_k += arr[new_i][new_j]
                    print(arr[new_i][new_j], end='|')

        print(f'>> {arr[i][j]} => {total_k + arr[i][j]}')



# N x M 배열에서 각 원소를 중심으로, 상하좌우의 k칸의 합계 중 최댓값은?
# 범위만 바꿔주면 된다.

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i, j in zip(di, dj):
    print(i, j)