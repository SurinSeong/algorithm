import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4875.txt'
sys.stdin = open(filename, 'r')


"""
맨 윗줄 : 3 출발
마지막 줄 : 2 도착
통로 : 0
도착 가능하면 1, 아니면 0
"""

# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    