# 후위식으로 변화되어 있는 경우
stack = [0]*100
top = -1

susik = '6528-*2/+'

for x in susik:
    if x not in '+-/*':     # 피연산자이면
        top += 1
        stack[top] = int(x)     # 스택에 넣어주기
    else:   # 연산자이면
        op2 = stack[top]    # 피연산자2 꺼내기
        top -= 1
        op1 = stack[top]    # 피연산자1 꺼내기
        top -= 1

        if x == '+':
            top += 1
            stack[top] = op1 + op2     # 계산 결과를 스택에 넣어주기
        elif x == '-':
            top += 1
            stack[top] = op1 - op2  # 계산 결과를 스택에 넣어주기
        elif x == '/':
            top += 1
            stack[top] = op1 / op2  # 계산 결과를 스택에 넣어주기
        elif x == '*':
            top += 1
            stack[top] = op1 * op2  # 계산 결과를 스택에 넣어주기

print(stack[top])
