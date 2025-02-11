import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_10804.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    str1 = list(input())[::-1]
    for i in range(len(str1)):
        if str1[i] == 'b':
            str1[i] = 'd'
        elif str1[i] == 'd':
            str1[i] = 'b'
        elif str1[i] == 'q':
            str1[i] = 'p'
        else:
            str1[i] = 'q'

    print(f'#{t} {"".join(str1)}')