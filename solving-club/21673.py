import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_21673.txt'
sys.stdin = open(filename, 'r')


def postfix(fx):
    
    stack = [0] * len(fx)
    top = -1
    
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}    # 스택 외부에서의 우선 순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}    # 스택 내부에서의 우선 순위
    
    new_fx = ''
    
    for x in fx:
        if x not in '(+-*/)':    # 연산자가 아니면
            new_fx += x
            
        elif x == ')':    # 닫는 괄호라면
            while stack[top] != '(':    # 여는 괄호가 나올 때까지
                new_fx += stack[top]
                top -= 1    # pop
            top -= 1    # '(' -> pop
        
        else:    # 그 외의 연산자라면
            if (top == -1) or (isp[stack[top]] < icp[x]):    # 스택에 아무것도 없거나 / 토큰의 우선순위가 높으면
                top += 1
                stack[top] = x    # push
            elif isp[stack[top]] >= icp[x]:    # 토큰의 우선순위가 낮으면 (else 가능)
                while (top > -1) and (isp[stack[top]] >= icp[x]):    # 스택에 아무것도 없어질 때까지나 / 토큰의 우선순위가 높아진다면
                    new_fx += stack[top]
                    top -= 1    # pop
                top += 1
                stack[top] = x    # 우선 순위 높은 것을 다 빼고 push
    
    # 혹시 스택에 있는 것이 다 나오지 않았다면
    while top > -1:
        new_fx += stack[top]
        top -= 1
                
    return new_fx


# 후위 유사 표기법
# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 중위 표기법으로 된 수식
    expression = input()
    # 후위 표기법으로 만들기
    result = postfix(expression)
    
    print(f'#{test_case} {result}')