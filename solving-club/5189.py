"""
[전자카트]
- 사무실 출발 -> 각 관리구역 -> 사무실
- 한번만 방문
- 최소 배터리 사용량

- 1 : 사무실
- 2 ~ N : 관리 구역 번호
"""
# import sys
#
# sys.stdin = open('./input/input_5189.txt', 'r')


# 1 빼고의 조합 구하기
def dfs(s, cnt, total):    # s : 시작, cnt : 횟수
    global answer

    # 더해가는 값이 이미 최솟값으로 구한 값보다 크다면
    if answer < total:
        return

    # 마지막 관리구역까지 가면 종료
    if cnt == N-1:
        total += battery[s][0]
        answer = min(answer, total)
        return

    for e in range(1, N):
        if not visited[e]:    # 방문한 적이 없음.
            visited[e] = True    # 방문 처리
            dfs(e, cnt + 1, total+battery[s][e])
            visited[e] = False


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 관리 구역들
    N = int(input())
    # 배터리 소비량 표
    battery = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    answer = 10000

    dfs(0, 0, 0)

    print(f'#{tc} {answer}')