# Ladder1
# 사다리 게임
# X에 도착하려면?
# 100x100
# 지정된 도착점에 대응되는 출발점 x 반환
# 사다리 : 1, 도착 : 2
# 사다리 시작 점이 없는 곳이 연결 구간이 있는 곳
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1210.txt'
sys.stdin = open(filename, 'r')


# 함수
# 오른쪽 이동
def find_end_of_right_one(i, j, matrix):
    pass


# 왼쪽 이등
def find_end_of_left_one(i, j, matrix):
    pass


def solve_ladder(matrix, i, j):
    # 맨 아래까지가서 끝남.
    while 0 <= i < 100:
        # 하나 내리기
        i += 1
        # 만약 오른쪽에 1이 있다면
        if ((0 <= j + 1 < 100) and (0 <= i < 100)) and (matrix[i][j + 1] == 1):
            # 어디까지 1이 있는지 찾아보기 -> 마지막 j값 받기
            j = find_end_of_one(i, j, matrix, 'r')
            # 한칸 내려가기
            i += 1
        # 만약 왼쪽에 1이 있다면
        elif ((0 <= j - 1 < 100) and (0 <= i < 100)) and (matrix[i][j - 1] == 1):
            # 어디까지 1이 있는지 찾아보기 -> 마지막 j값 받기
            j = find_end_of_one(i, j, matrix, 'l')
            # 한칸 내려가기
            i += 1



    if matrix[i-1][j] == 2:
        return j
    return 0


# 테스트 케이스
for _ in range(10):
    # 테스트케이스 번호
    t = int(input())
    # 100x100 matrix 받기
    puzzle = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        # 만약 첫 번째가 0이면 길이 없음.
        if puzzle[0][x] == 0:
            continue
        # 1이면 길찾기 시작
        result = solve_ladder(puzzle, 0, x)

        if result != 0:
            break

    print(f'#{t} {result}')
