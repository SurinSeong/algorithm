"""
[홈 방범 서비스]
- N*N
- 마름모

- 홈 방범 서비스를 제공 받는 집들은 각각 M의 비용을 지불 할 수 있음.
- 운영 비용 = K * K + (K - 1) * (K - 1)
- 도시의 크기 N, 하나의 집이 지불할 수 있는 비용 M, 도시 정보
- 홈 방범 서비스를 제공 받는 집들의 수 출력

- 보안회사가 손해를 보지 않고 서비스 가능한 최대 집의 수
- 보안회사의 이익 = 서비스 제공받는 집들을 통해 얻는 수익 - 운영 비용
"""
import sys

sys.stdin = open('./input/input_2117.txt', 'r')

# 서비스 가능한 집의 개수 구하기
def find_available_houses(cj, ci):
    houses = 0
    visited = [[0]*N for _ in range(N)]
    # 중앙에서 최대로 갈 수 있는 거리
    for d in [1, -1]:    # 우 -> 좌
        for k in range(0, K):
            nj = cj + d*k
            if 0 <= nj < N:    # 범위 안에 있다면
                max_j = K - k
                for di in range(0, max_j):
                    up_i, down_i = ci - di, ci + di
                    if (0 <= up_i < N):
                        if (city[up_i][nj] == 1) and (visited[up_i][nj] == 0):    # 범위 안에 있고 집이 있다면, 방문한 적이 없다면
                            houses += 1
                            visited[up_i][nj] = 1

                    if (0 <= down_i < N):
                        if (city[down_i][nj] == 1) and (visited[down_i][nj] == 0):
                            houses += 1
                            visited[down_i][nj] = 1
            max_j -= 1

    return houses


# 도시에 있는 모든 집 개수 확인
def find_houses():
    total_houses = 0

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                total_houses += 1

    return total_houses


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())

    # 도시 정보 (1 : 집)
    city = [list(map(int, input().split())) for _ in range(N)]

    # 현재 도시의 모든 집의 개수
    total_houses = find_houses()
    # 가능한 순수익
    available_profit = total_houses * M

    # 최소 서비스 가능 집의 수
    answer = 1

    K = 2
    while True:    # 서비스 운영비용 마이너스가 되지 않을 때까지

        # 운영 비용
        operate_expense = K*K + (K-1)*(K-1)

        if operate_expense > available_profit:   # 운영 비용이 서비스 수익보다 크면
            break    # 끝내기

        for r in range(N):
            for c in range(N):
                service_houses = find_available_houses(c, r)    # 서비스 가능한 집의 수
                profit = service_houses * M - operate_expense    # 수익

                if profit >= 0:    # 손해를 보지 않았다면
                    answer = max(service_houses, answer)

        K += 1

    print(f'#{tc} {answer}')