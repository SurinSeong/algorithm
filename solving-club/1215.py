import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1215.txt'
sys.stdin = open(filename, 'r')


#  가로 세로 전부 찾아보기
def find_palindrome(arr, n):
    # 회문 개수
    palindrome = 0

    for i in range(8):
        for j in range(8-n+1):
            check_word = arr[i][j:j+n]
            # 회문의 절반 길이 만큼 비교
            for k in range(n//2):
                # 양 끝부터 비교
                if check_word[k] != check_word[n-k-1]:
                    break
            else:
                palindrome += 1

    return palindrome

for t in range(1, 11):
    # 회문의 길이
    N = int(input())
    
    matrix = [list(input()) for _ in range(8)]
    # 전치
    matrix_T = list(map(list, zip(*matrix)))

    result1 = find_palindrome(matrix, N)
    result2 = find_palindrome(matrix_T, N)

    print(f'#{t} {result1 + result2}')