import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4874.txt'
sys.stdin = open(filename, 'r')

# Forth
# 후위식 계산법 적용하기
# 마침표 : 출력
# error : 토큰이 연산자인데 남은 피연산자가 2개 미만일 경우
# 마침표가 나왔는데 피연산자가 2개 이상 또는 0개


def calculator(string):
    # 스택
    stack = [0] * 256
    top = -1
    
    for x in string:

        if x not in '.+-*/':     # 피연산자이면
            top += 1
            stack[top] = x      # push

        elif x != '.':   # 연산자이면
            
            if top == 0:
                return 'error'
            
            op2 = int(stack[top])    # pop
            top -= 1
            op1 = int(stack[top])    # pop
            top -= 1

            # 연산자 종류 확인
            if x == '+':
                top += 1
                stack[top] = op1 + op2      # 계산 후 push
            elif x == '-':
                top += 1
                stack[top] = op1 - op2      # 계산 후 push
            elif x == '*':
                top += 1
                stack[top] = op1 * op2      # 계산 후 push
            elif x == '/':
                top += 1
                stack[top] = op1 / op2      # 계산 후 push
        
        else:    # 마지막이 .이라면
            break
            
    if top == 0:
        return int(stack[top])
    
    return 'error'
    

# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 연산 코드
    postfix = input().split()

    result = calculator(postfix)

    print(f'#{test_case} {result}')