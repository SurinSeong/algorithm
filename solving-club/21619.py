import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_21619.txt'
sys.stdin = open(filename, 'r')

# 괄호 검사 맞으면 1, 아니면 -1
# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    brackets = input()
    # 스택 준비 (괄호 개수)
    N = len(brackets)
    stack = [0]*N
    # top 설정
    top = -1
    # 결과
    result = 1
    # 반복문 돌리기
    for char in brackets:
        # 만약 '('라면
        if char == '(':
            # top 증가시키고, stack에 넣어준다
            top += 1
            stack[top] = char
        # ')' 라면
        elif char == ')':
            # 만약 stack이 비어있다면
            if top == -1:
                # 맞지 않은 구성이다.
                result = -1
                break
            # 비어있지 않다면
            else:
                # pop
                top -= 1

    # 다 돌았는데 stack에 남아있는 것이 있을 경우
    if top != -1:
        result = -1

    print(f'#{tc} {result}')
