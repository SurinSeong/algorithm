import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1222.txt'
sys.stdin = open(filename, 'r')

# 계산기1
# 문자열로 이루어진 계산식
# 후위 표기식으로 바꾸어 계산하기
# 연산자를 + 하나
# 피연산자는 0~9

def change_to_postfix(expression, n):
    # 스택
    stack = [0]*n
    top = -1
    
    new_fx = ''
    
    for x in expression:
        if x != '+':    # 연산자가 아니라면
            new_fx += x
        
        else:    # 연산자라면
            while True:
                if top == -1:
                    top += 1
                    stack[top] = x    # push
                    break
                
                new_fx += stack[top]
                top -= 1
                
    new_fx += stack[top]
    
    return new_fx


def calculator(expression, n):
    postfix = change_to_postfix(expression, n)
    
    # 스택
    stack = [0] * n
    top = -1
    
    for x in postfix:
        if x != '+':    # 연산자가 아니라면
            top += 1
            stack[top] = int(x)
        
        else:    # 연산자라면
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            
            total = op1 + op2
            
            top += 1
            stack[top] = total
            
    return stack[top]         
            

for test_case in range(1, 11):
    # 문자열 계산식의 길이
    N = int(input())
    
    # 계산식
    fx = input()
    
    result = calculator(fx, N)
    
    print(f'#{test_case} {result}')