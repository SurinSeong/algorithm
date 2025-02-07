# 파리퇴치

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # N, M
    N, M = map(int, input().split())
    # matrix 받기
    flies = [list(map(int, input().split())) for _ in range(N)]

    # flies 돌기
    max_total = 0
    # 행
    for i in range(N-M+1):
        # 열
        for j in range(N-M+1):
            # M x M의 합 구하기 >>> i ~ i+M / j ~ j+M
            total = 0
            for mi in range(i, i+M):
                for mj in range(j, j+M):
                    total += flies[mi][mj]
            # 최대 구하기
            if max_total < total:
                max_total = total

    print(f'#{t} {max_total}')
