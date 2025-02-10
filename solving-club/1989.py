# 회문
# 회문이면 1, 아니면 0
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1989.txt'
sys.stdin = open(filename, 'r')


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # word
    word = input()
    
    if word == word[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')