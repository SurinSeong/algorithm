# 단순 이진 암호 코드
# 16진수 >> 2진수 변환 필요
# 배열에는 하나 이상의 암호 코드가 존재함. >> 모든 코드가 정상적인 암호코드임을 보장할 수 없음.
# 올바른 암호코드의 값만 더하기

"""
[조건]
- 암호 코드들이 붙어있는 경우는 없음.
- 0의 개수, 1의 개수를 찾고 비율을 찾아야 함. (가장 작은 값으로 나눠준다.) --> 0자리는 고려하지 않아도 된다.
- 각 암호코드의 둘레에는 최소 1칸 이상의 빈공간이 존재한다.
"""
import sys

sys.stdin = open('./input/input_1242.txt', 'r')

# 16진수의 시작과 끝 찾기
def find_start(fi):
    for i in range(fi, N):
        for j in range(M):
            if matrix[i][j] != '0':    # 시작 col 인덱스
                sj = j
                break
        else:
            continue

        for nj in range(sj, M):
            if matrix[i][nj] == '0':    # 끝 col 인덱스
                ej = nj
                break

        si = i    # 시작 row 인덱스
        for ni in range(si+1, N):    # 끝 row 인덱스
            if matrix[ni][sj] == '0':
                ei = ni
                break

        return si, ei, sj, ej


# 찾은 16진수를 0으로 바꿔준다.
def change_to_zero(si, ei, sj, ej):
    # 16진수가 있는 범위
    for i in range(si, ei):
        for j in range(sj, ej):
            matrix[i][j] = '0'

# 1. 16진수를 2진수로 바꿔서 넣어준다.
# 2. 뒤에서 1을 찾아준다.


# 테스트 케이스 받기
T = int(input())

for tc in range(1, T+1):
    # 세로, 가로
    N, M = map(int, input().split())
    # 배열값
    matrix = [list(input()) for _ in range(N)]

    answer = 0

    code_list = []

    fi = 0    # 탐색 시작 행
    # 암호 찾기
    while fi < N:
        # 종료 조건
        standard = matrix[0]

        # 1. 시작 col 인덱스, 마지막 col 인덱스
        si, ei, sj, ej = find_start(fi)

        # 2. 코드 리스트에 해당 행을 넣어준다.
        code_list.append(matrix[si])

        # 3. 같은 배열 바꿔주기 => 왜냐면 다른 코드를 또 찾아야 하니깐
        change_to_zero(si, ei, sj, ej)

        # 탐색 시작 행의 인덱스 업데이트
        fi = si



    print(f'#{tc} {answer}')