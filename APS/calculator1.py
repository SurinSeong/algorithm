# 연습 문제1
"""
- 2 + 3 * 4 / 5 => 234*5/+
- 2 + 3 * 4 + 5 => 234*+5+
"""
# 중위식을 후위식으로 바꾸기
stack = [0] * 100
top = -1

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택 외부에서의 토큰의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택 내부에서의 토큰의 우선순위

fx = '(6+5*(2-8)/2)'

susik = ''

for x in fx:
    if x not in '(+-*/)':   # 피연산자
        susik += x
    elif x == ')':      # 닫는 괄호
        while stack[top] != '(':    # 여는 괄호가 나올 때까지
            susik += stack[top]
            top -= 1
        top -= 1
    else:
        if (top == -1) or (isp[stack[top]] < icp[x]):     # 스택에 아무것도 없거나 토큰의 우선순위가 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:     # 토큰의 우선 순위가 낮으면 (else 가능)
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]     # 우선순위가 높은 것들을 pop
                top -= 1
            top += 1
            stack[top] = x      # 그 후에 push

print(susik)