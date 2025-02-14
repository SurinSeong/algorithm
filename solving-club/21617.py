# 괄호 검사
# 종류가 다르다
# {}, ()
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_21617.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 괄호모음 받기
    brackets = input()
    # top 설정
    top = -1
    N = len(brackets)
    # 스택 만들기
    stack = [0]*N
    # 결과
    result = 1
    # 반복문
    for bracket in brackets:
        # '(', '{' 이라면
        if (bracket == '(') or (bracket == '{'):
            # top 넣어주고
            top += 1
            # 스택 쌓기
            stack[top] = bracket
        # ')' 이라면
        elif bracket == ')':
            # 빈 스택이라면
            if top == -1:
                # 비정상
                result = 0
                # 끝내기
                break
            # stack[top]이 다른 종류라면
            elif stack[top] == '{':
                # 비정상
                result = 0
                # 끝내기
                break
            # 같은 종류라면
            else:
                # pop
                top -= 1
        # '}' 이라면
        elif bracket == '}':
            # 빈 스택이라면
            if top == -1:
                # 비정상
                result = 0
                # 끝내기
                break
            # stack[top]이 다른 종류라면
            elif stack[top] == '(':
                # 비정상
                result = 0
                # 끝내기
                break
            # 같은 종류라면
            else:
                # pop
                top -= 1
    # 다돌았는데 stack에 뭔가가 있다면
    if top != -1:
        # 비정상
        result = 0

    print(f'#{tc} {result}')

