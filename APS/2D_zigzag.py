# 지그재그 순회
# 어떻게 하면 역순으로 갈 수 있을지 생각해보기
# 먼저, N, M 입력 받기
N, M = map(int, input().split())

# arr 받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 지그재그
for i in range(N):
    for j in range(M):
        new_j = j + (M - 1 - 2*j) * (i % 2)
        print(arr[i][new_j])


# 위아래
for i in range(N):
    for j in range(M):
        if j % 2:
            print(arr[i][j])
        else:
            print(arr[N - 1 - i][j])

        print(arr[i + (N - 1 - 2*i) * (j % 2)][j])

# 대각선 왔다갔다 순회
