import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4408.txt'
sys.stdin = open(filename, 'r')

"""
최단 시간에 모든 학생이 자신의 방으로 돌아간다.
방 : 400개
복도가 겹치면 같이 못들어감.
"""
def go_back(arr, n):
    stack = []
    stack.append(arr[0])

    while True:






# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    # 들어가야 할 학생 리스트
    student_list = []
    # 학생 수 만큼 반복
    for _ in range(N):
        here, move = map(int, input().split())
        student_list.append([here, move])

    answer = 0

    print(f'#{tc} {answer}')