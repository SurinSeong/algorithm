"""
[최적 경로]
- 회사 출발, N명의 고객 방문 후 자신의 집으로 돌아간다. (2 <= 고객 <= 10)
- 2차원 최대 100 x 100
- 위치 사이의 거리는 절댓값 플러스
- 모두 방문 & 가장 짧은 경로는?
"""
def dfs(cnt, total, si, sj):
    global ex, ey, answer

    if total > answer:
        return

    if cnt == N:
        # 집과의 거리 구하기
        total += (abs(si-ex) + abs(sj-ey))
        answer = min(answer, total)
        return

    for i in range(N):
        if not visited[i]:    # 방문하지 않았다면
            visited[i] = True
            ni, nj = customers[i][0], customers[i][1]
            distance = abs(si-ni) + abs(sj-nj)
            dfs(cnt+1, total+distance, ni, nj)
            visited[i] = False


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 고객 수
    N = int(input())

    # 고객 좌표 넣는 리스트
    customers = [0] * N

    # 방문 확인용
    visited = [False] * N

    # 회사의 좌표, 집의 좌표, N명의 고객 좌표
    points = list(map(int, input().split()))

    for n in range(len(points)//2):
        x = points[n*2]
        y = points[n*2+1]
        # 회사 좌표
        if n == 0:
            sx, sy = x, y
        # 집 좌표
        elif n == 1:
            ex, ey = x, y
        # 고객 좌표
        else:
            customers[n-2] = [x, y]

    answer = 10000

    # 순열 구해서
    # 최소 이동거리 찾기
    dfs(0, 0, sx, sy)

    print(f'#{tc} {answer}')


