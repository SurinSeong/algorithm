import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1225.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 암호 생성기
"""
8개의 숫자
첫번째를 -1한 후 맨 뒤로, 두 번째를 -2한 후 맨 뒤로 ... 다섯 번째를 -5 한 후 맨 뒤로
숫자가 감소할 때, 0보다 작아지는 경우 0으로 유지
==> 프로그램 종료
"""
def make_password(arr):
    minus = -1
    while True:
        minus = (minus+1) % 5   # 1~5가 한세트

        first = arr.popleft()   # 가장 첫번째 값 빼기
        first -= (minus+1)    # 싸이클에 맞게 빼기

        if first <= 0:    # 0이거나 음수이면
            arr.append(0)    # 0을 뒤에 넣기
            break    # 끝내기

        arr.append(first)    # 양수이면

    return arr

# 테스트 케이스 개수
T = 10

for _ in range(T):
    tc = int(input())
    numbers = list(map(int, input().split()))    # 8개의 숫자 받기
    numbers = deque(numbers)    # deque로 변경

    # 숫자 사이클 돌면서 바꾸기
    result = make_password(numbers)

    print(f'#{tc} {" ".join(list(map(str, result)))}')