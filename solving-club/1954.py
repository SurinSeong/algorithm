# 달팽이 숫자 >> 다시..
# 1~N*N 숫자가 시계방향으로 작성
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1954.txt'
sys.stdin = open(filename, 'r')


def make_snail(i, j, arr, n):
    # 끝날 때까지 반복한다.
    # 오른쪽 요소가 범위 안에 있고, 0이라면
    if ((0 <= i+1 < n) and (0 <= j+1 < n)) and ((arr[i][j+1] == 0) and (arr[i-1][j+1] != 0) or (0 > i-1)):
        # 현재의 칸의 값에 1 추가
        arr[i][j+1] = (arr[i][j] + 1)
        return make_snail(i, j+1, arr, n)

    # 아래의 요소가 범위 안에 있고, 0이라면
    elif ((0 <= i+1 < n) and (0 <= j < n)) and arr[i+1][j] == 0:
        # 현재의 칸의 값에 1 추가
        arr[i+1][j] = (arr[i][j] + 1)
        return make_snail(i+1, j, arr, n)

    # 왼쪽의 요소가 범위 안에 있고, 0이라면
    elif ((0 <= i < n) and (0 <= j-1 < n)) and arr[i][j-1] == 0:
        # 현재의 칸의 값에 1 추가
        arr[i][j-1] = (arr[i][j] + 1)
        return make_snail(i, j-1, arr, n)

    # 위쪽의 요소가 범위 안에 있고, 0이라면
    elif ((0 <= i-1 < n) and (0 <= j < n)) and (arr[i-1][j] == 0 and arr[i-1][j+1] == 0):
        # 현재의 칸의 값에 1 추가
        arr[i-1][j] = (arr[i][j] + 1)
        return make_snail(i-1, j, arr, n)



# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # N
    N = int(input())
    # 빈 매트릭스 만들기
    matrix = [[0]*N for _ in range(N)]
    # 우선 가장 첫 번째에 1을 넣어준다.
    matrix[0][0] = 1
    # 달팽이 매트릭스 만들기
    make_snail(0, 0, matrix, N)

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()