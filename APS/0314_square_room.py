"""
접근방법 1. 모든 방에서 출발해 최대한 이동해본다.
    - 재귀호출 사용
        1) 시간
        2) maximum recursion
        => 위의 두 가지를 꼭 기억하기

접근방법 2.
- 1부터 N**2을 인덱스로 갖는 배열 A를 만든다. (2차원 배열을 1차원으로 만들기)
- 숫자 i의 인접에 1큰 수가 있는 경우 A[i]에 1을 표시한다.
- 연속한 1의 개수가 가장 긴 것을 찾는다.

==> 응용하기 좋다!
"""
# 연속된 1의 길이가 가장 긴 구간이 정답이다.

# 방의 개수 만큼 탐색
# 델타 설정 후 특정 방에서 델타 탐색 진행
    # 범위 체크
    # 현재 방 숫자 + 1인 방이 나오면 1 기록하기
        # 나머지는 볼 필요가 없음
# -------------------------------------------------------
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    # 방들 개수
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 2차원을 1차원으로 만들어주기
    visited = [0] * (N**2+1)

    for i in range(N):
        for j in range(N):
            for d in range(4):    # 현재 위치 숫자 기준 상하좌우 확인하기
                ni, nj = i + dy[d], j + dx[d]
                if 0 <= ni < N and 0 <= nj < N:    # 범위에 있다면
                    if rooms[ni][nj] == rooms[i][j] + 1:    # 이동 가능하다면
                        visited[rooms[i][j]] = 1    # 방문기록에 표시하기
                        break
    answer = 1
    cnt = 1
    start = 0

    # visited 확인하기
    for i in range(1, N**2+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if cnt > answer:
                answer = cnt
                start = i - (cnt - 1)   # 최댓값..
            cnt = 1

    print(f'#{tc} {start} {answer}')