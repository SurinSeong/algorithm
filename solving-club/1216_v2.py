# 회문 2
# 가로 세로를 모두 보아 가장 긴 회문의 길이 구하기
# 100x100

import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1216.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


# 함수 ==> 다른 방법으로 해보기 ****************
# 한줄만 비교해보기
def search_palindrome(arr, n):
    # 최소 길이
    max_length = 1
    # row 하나씩 탐색
    for start in range(N-1):
        row_


    return max_length


for _ in range(10):
    # 테스트 케이스 번호
    t = int(input())
    # 100x100 받기
    N = 100
    matrix = [list(input()) for _ in range(N)]
    matrix_T = list(map(list, zip(*matrix)))
    # 가장 길이가 긴 회문의 길이
    result1 = search_palindrome(matrix, N)
    result2 = search_palindrome(matrix_T, N)

    print(f'#{t} {max(result1, result2)}')
