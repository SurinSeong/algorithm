"""
[격자판의 숫자 이어붙이기]
- 4x4
    - 0 ~ 9
- 임의의 위치에서 시작해서 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동
    - 각 칸에 적혀있는 숫자를 차례로 이어붙이면 7자리의 수

- 한번 갔던곳 또 가도 된다.
- 0으로 시작하는 수도 만들 수 있다.
"""
def make_subset(si, sj, subset):
    if len(subset) == 7:
        total_subset_list.add(''.join(map(str, subset)))
        return

    for d in range(4):
        ni, nj = si + dy[d], sj + dx[d]
        if 0 <= ni < 4 and 0 <= nj < 4:    # 범위 안에 있다면
            make_subset(ni, nj, subset+[matrix[ni][nj]])


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 격자판 정보
    matrix = [list(map(int, input().split())) for _ in range(4)]

    answer = 0

    total_subset_list = set()    # 총 숫자 리스트

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for i in range(4):
        for j in range(4):
            make_subset(i, j, [matrix[i][j]])

    answer = len(total_subset_list)

    print(f'#{tc} {answer}')