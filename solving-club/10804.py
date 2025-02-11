import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_10804.txt'
sys.stdin = open(filename, 'r')


# 문자열 바꾸는 함수
def in_mirror(target):
    if target == 'b':
        return 'd'
    if target == 'd':
        return 'b'
    if target == 'q':
        return 'p'
    if target == 'p':
        return 'q'


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    str1 = list(input())
    # 전체 길이의 절반만 사용
    for i in range(len(str1)//2):
        str1[i], str1[len(str1)-1-i] = in_mirror(str1[i]), in_mirror(str1[len(str1)-1-i])

        str1[i], str1[len(str1)-1-i] = str1[len(str1)-1-i], str1[i]
    # 홀수면
    if len(str1) % 2:
        str1[len(str1)//2] = in_mirror(str1[len(str1)//2])

    print(f'#{t} {"".join(str1)}')