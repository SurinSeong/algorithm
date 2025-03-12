"""
[최소합]
- NxN
- 우하 이동 가능
- 맨 왼쪽 위에서 오른쪽 아래까지
- 가능한 모든 경로에 대해 합을 계산한 후 최솟값 찾아도 된다.
"""
def dfs(i, j, total):
    global answer

    # 더한 게 답보다 크면
    if answer <= total:
        return

    # 마지막 칸에 도착하면
    if i == N-1 and j == N-1:
        answer = min(answer, total)
        return

    for d in range(2):
        ni, nj = i + dy[d], j + dx[d]

        if 0 <= ni < N and 0 <= nj < N:    # 배열 범위 안에 있다면
            dfs(ni, nj, total+matrix[ni][nj])




# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 가로, 세로
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dy = [0, 1]
    dx = [1, 0]

    answer = 1690

    dfs(0, 0, matrix[0][0])

    print(f'#{tc} {answer}')