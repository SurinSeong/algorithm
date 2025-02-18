import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5432.txt'
sys.stdin = open(filename, 'r')

# 여러 개의 쇠막대기를 레이저로 절단.
"""
쇠막대기는 자신보다 긴 막대기 위에만 놓일 수 있다.
쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록
쇠막대기를 자르는 레이저는 적어도 하나 존재
레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음.
- 레이저 : ()
- 쇠막대기 : (    )
"""

def count_pipes(string):
    # 스택 생성
    stack = [0]*len(string)
    top = -1

    for x in string:
        if x == '(':    # 열린 괄호라면
            top += 1
            stack[top] = x
        else:   # 닫힌 괄호라면
            top -= 1



T = int(input())

for test_case in range(1, T+1):
    # 괄호 뭉텅이
    bracket = input()

    result = 0

    print(f'#{test_case} {result}')
