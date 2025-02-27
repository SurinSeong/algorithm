# import sys
# from pathlib import Path
#
# filename = Path.cwd() / 'solving-club/input/input_1949.txt'
# sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[등산로 조성]
- 부지 : NxN
- 목표 : 최대한 긴 등산로
- 숫자 : 지형의 높이

[규칙]
- 가장 높은 봉우리
- 높은 지형에서 낮은 지형으로 가로-세로 연결
- 딱 한 곳을 최대 K 깊이까지 깎는다.

[제약 사항]
- 3 <= N <= 8
- 1 <= K <= 5
- 1 <= 지형의 높이 <= 20
"""
# 시작 시간 : 14:15 ~
# 가장 높은 곳의 높이 찾는 함수
def find_max_heights(arr, n):
    max_height = 0
    for i in range(n):
        for j in range(n):
            max_height = max(max_height, arr[i][j])

    return max_height


# 가장 높은 곳의 인덱스 찾는 함수
def find_highest_idx(arr, n):
    idx_list = []

    max_h = find_max_heights(arr, n)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_h:
                idx_list.append([i, j])

    return idx_list


# 안 깎고 이동시키기
def dfs(si, sj, n):
    global max_move

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 스택 만들기
    stack = []
    visited = [[0]*N for _ in range(N)]
    # 출발 위치 넣기
    stack.append([si, sj])
    visited[si][sj] = 1

    while stack:
        ci, cj = stack.pop()

        # 갈 수 있는 곳 찾아보기
        for di, dj in delta:
            if (0 <= ci+di < n) and (0 <= cj+dj < n):    # 배열 안에 있다면
                if mountain[ci][cj] > mountain[ci+di][cj+dj]:    # 현재 위치보다 낮다면
                    if visited[ci+di][cj+dj] == 1:    # 방문한 적이 있다면 건너뛰기
                        continue

                    # 방문한 적이 없다면
                    stack.append([ci, cj])    # 기존의 위치 넣어주고
                    stack.append([ci+di, ci+dj])    # 다음 위치도 넣어준다.
                    visited[ci+di][cj+dj] = 1    # 방문 기록 업데이트
                    break

        # 갈 수 있는 곳이 없다면
        else:
            max_move = max(max_move, len(stack)+1)






# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 한 변의 길이, 최대 공사 가능 깊이
    N, K = map(int, input().split())
    # 지형 정보
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 지형들 찾기
    highest_locations = find_highest_idx(mountain, N)

    max_move = 0

    for i, j in highest_locations:
        dfs(i, j, N)

    print(max_move)