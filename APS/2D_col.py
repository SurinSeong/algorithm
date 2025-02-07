# 열 우선 순회
# N, M 받기
N, M = map(int, input().split()) # 행 개수, 열 개수 순으로 입력 받는다.

# arr 만들기
arr = [list(map(int, input().split())) for _ in range(N)]

# 열 우선 순회 하기
for j in range(M):
    for i in range(N):
        print(arr[i][j])
