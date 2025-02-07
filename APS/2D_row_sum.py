# N X M 배열의 크기와 저장된 값이 주어질 때, 합을 구하는 방법
# 먼저, N, M 입력 받기
N, M = map(int, input().split())

# arr 받기
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
# 배열의 총합 구하기
for i in range(N):
    for j in range(M):
        total += arr[i][j]

print(total)

# 행의 합이 최대인 행은?
max_row = 0

for i in range(N):
    current_row = 0
    for j in range(M):
        current_row += arr[i][j]

    if max_row < current_row:
        max_row = current_row
        max_row_idx = i

print(i, max_row)

