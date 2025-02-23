import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1223.txt'
sys.stdin = open(filename, 'r')

# 계산기2
"""
1. 후위 표기식으로 바꾸기
2. 계산하기

연산자 : '*+'
"""
def to_postfix(string, n):
    answer = ''
    # 스택 설정
    stack = []
    top = -1
    
    # 우선순위
    ip = {'*': 3, '+': 1}
    
    for x in string:
        if x not in '*+':    # 피연산자 이면
            answer += x
            
        else:    # 연산자 이면
            if (top == -1) or (ip[stack[top]] < ip[x]):    # 현재의 연산자의 우선순위가 스택 안의 연산자의 우선순위보다 높으면
                top += 1
                stack.append(x)
                
            elif ip[stack[top]] >= ip[x]:    # 현재의 연산자의 우선순위가 스택안의 연산자의 우선순위보다 낮으면
                
                while (top > -1) and (ip[stack[top]] >= ip[x]):
                    answer += stack.pop()    # 현재의 연산자 우선순위가 높아질 때까지 스택 안의 연산자를 빼낸다.
                    top -= 1
                    
                top += 1
                stack.append(x)    # 다시 넣어준다.
                
    while top > -1:    # 스택 안의 것을 다시 빼서 후위식으로 넣어준다.
        answer += stack.pop()
        top -= 1
            
    return answer


def calculator(string, n):
    # 후위식 생성
    postfix = to_postfix(string, n)
    
    # 스택 생성
    stack = []
    
    for x in postfix:
        if x not in '+*':    # 피연산자라면
            stack.append(x)
        
        else:    # 연산자라면
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            
            if x == '+':
                stack.append(op1+op2)
            elif x == '*':
                stack.append(op1*op2)
    
    result = stack.pop()
    
    return result


# 테스트 케이스
T = 10

for tc in range(1, T+1):
    # 테스트 케이스 길이
    N = int(input())
    # 중위식
    expression = input()
    
    result = calculator(expression, N)
    
    print(f'#{tc} {result}')