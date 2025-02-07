# N x M
# 어떤 풍선을 터뜨리면 풍선이 추가로 터진다. => 본인, 상하좌우
# 하나의 풍선을 선택해 터뜨렸을 때, 날릴 수 있는 꽃가루 수 중 최대?

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # N, M
    N, M = map(int, input().split())
    # matrix 받기
    balloons = [list(map(int, input().split())) for _ in range(N)]
    # 최대 꽃가루
    max_sum = 0
    # 행
    for i in range(N):
        # 열
        for j in range(M):
            # 특정 좌표에서의 합
            total = 0
            # 우하좌상
            delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for di, dj in delta:
                new_i, new_j = i + di, j + dj
                # 조건 맞는지 확인
                if (0 <= new_i < N) and (0 <= new_j < M):
                    # 맞으면 더하기
                    total += balloons[new_i][new_j]
            # 자기 자신도 더해주기
            total += balloons[i][j]
            
            # max_sum 과 비교하기
            # if max_sum < total:
            #     max_sum = total
            max_sum = max(max_sum, total)

    print(f'#{t} {max_sum}')

