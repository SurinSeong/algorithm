# 현주의 상자 바꾸기
# 1 ~ N => N개의 상자
# 처음에는 0으로 적혀있음.
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# i번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5789.txt'
sys.stdin = open(filename, 'r')


# 테스트 케이스 개수
T = int(input())

for x in range(1, T+1):
    # 상자 개수, 변경 가능 횟수
    N, Q = map(int, input().split())
    # 빈 상자 리스트 만들기
    boxes = [0]*N
    # 변경 횟수만큼 반복
    for q in range(1, Q+1):
        # L ~ R
        L, R = map(int, input().split())
        for i in range(L-1, R):
            boxes[i] = q
    # 출력
    print(f'#{x} {" ".join([str(box) for box in boxes])}')
    