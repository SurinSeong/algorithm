# String
# 특정 문자열의 개수를 반환하는 프로그램
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1213.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


for _ in range(10):
    # 테스트 케이스 번호
    tc = int(input())
    # 찾아야하는 문자열
    pattern = input()
    # 주어진 문자열
    text = input()
    # 총 개수
    total = 0
    # 계속 찾을 수 있을 때까지 반복함.
    while text.find(pattern) != -1:
        pattern_loc = text.find(pattern)
        text = text[pattern_loc+len(pattern):]
        total += 1

    print(f'#{tc} {total}')