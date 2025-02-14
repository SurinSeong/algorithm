# 회문 2
# 가로 세로를 모두 보아 가장 긴 회문의 길이 구하기
# 100x100
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1216.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


# 함수
def search_palindrome(arr, n):
    # 최소 길이
    max_length = 1
    # row 하나씩 탐색
    for i in range(n):
        # 각 행에서의 끝점 : 가장 긴 길이부터 시작
        for end in range(N-1, 0, -1):
            # 각 행에서의 시작점
            for start in range(0, end):
                word_length = end - start + 1
                if arr[i][start:end+1] == arr[i][start:end+1][::-1]:
                    max_length = max(max_length, word_length)
                    break

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
