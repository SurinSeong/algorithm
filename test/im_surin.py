import sys

sys.stdin = open('../../../../Downloads/Sample_input.txt', 'r')

"""
공 굴리기 게임
NxN => 공이 가장 멀리 이동할 수 있는 거리는?
상하좌우
현재 높이보다 낮은 곳으로만 이동 가능, 그 중 가장 낮은 곳으로 이동
가장 멀리 이동할 수 있는 위치 찾아야 함.
높이는 모두 다르다.
"""
# 가장 낮은 높이 찾아서 반환
def find_lowest_height(arr, r, c, n):

    # 본인이 가장 낮다고 설정하기
    min_h = arr[r][c]
    min_r, min_c = r, c   # 가장 낮은 높이의 좌표

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dr, dc in delta:
        new_r, new_c = r + dr, c + dc
        if (0 <= new_r < n) and (0 <= new_c < n):    # 범위 안에 있다면 확인하기
            if min_h > arr[new_r][new_c]:
                min_h = arr[new_r][new_c]
                min_r, min_c = new_r, new_c   # 가장 낮은 높이의 좌표 업데이트

    return min_r, min_c


# 낮은 높이로 이동하기
def move_to_lowest_height(arr, r, c, n, cnt):
    low_r, low_c = find_lowest_height(arr, r, c, n)

    if (low_r == r) and (low_c == c):
        return cnt

    return move_to_lowest_height(arr, low_r, low_c, n, cnt+1)


T = int(input())

for test_case in range(1, T+1):
    # 배열의 크기
    N = int(input())
    # 배열
    heights = [list(map(int, input().split())) for _ in range(N)]

    long_distance = 0   # 갈 수 있는 최소 거리

    for i in range(N):
        for j in range(N):
            current_distance = move_to_lowest_height(heights, i, j, N, 1)
            long_distance = max(current_distance, long_distance)

    print(f'#{test_case} {long_distance}')