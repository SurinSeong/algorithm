import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_21618.txt'
sys.stdin = open(filename, 'r')

# 문자열 s에서 반복된 문자 지우기
# 지워진 부분은 앞뒤를 연결한다.
# 또 생기면 또 지운다.
# 남은 문자열의 길이는?
# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 문자열 받기
    s = input()
    # 스택 준비
    N = len(s)
    stack = [0]*N
    top = -1
    cnt = 0
    # 반복하면서 넣는다.
    for c in s:
        # 아무것도 없으면 넣어준다.
        if top == -1:
            top += 1
            stack[top] = c
        # stack의 peek와 c가 다르면 넣어준다.
        elif stack[top] != c:
            top += 1
            stack[top] = c
        # stack의 peek와 c가 같으면 뺀다.
        elif stack[top] == c:
            top -= 1
            # 겹치는 거는 2개니깐
            cnt += 2
    # 전체 길이에서 총 뺀 문자개수 빼주기
    result = N - cnt

    print(f'#{tc} {result}')
