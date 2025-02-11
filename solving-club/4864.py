# 문자열 비교
# 두 개의 문자열 str1, str2
# str2 안에 str1과 일치하는 부분이 있는지 찾기
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4864.txt'
sys.stdin = open(filename, 'r')


# # 함수
# def find_string(target, main):
#     if target in main:
#         return 1
#     return 0


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    for i in range(M-N+1):
        check_word = str2[i:i+N]
        if check_word == str1:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')


