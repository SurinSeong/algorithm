import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1234.txt'
sys.stdin = open(filename, 'r')

# 0~9로 이루어진 번호 문자열
# 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호
# 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거

for tc in range(1, 11):
    N, password = input().split()
    # N을 숫자로 바꿔주기
    N = int(N)
    # 스택 준비
    stack = ['_']*N
    top = -1
    # 반복
    for i in range(N):
        # 스택에 아무것도 없으면
        if top == -1:
            # 넣어주기
            top += 1
            stack[top] = password[i]
        # 스택에 무엇인가가 있다면
        else:
            # 같은 것인지 비교
            if password[i] == stack[top]:
                # stack을 활용하려고 pop을 해준다.
                stack.pop(top)
                top -= 1

            # 같지 않으면 넣어주기
            else:
                top += 1
                stack[top] = password[i]

    print(f'#{tc} {"".join(stack[:top+1])}')

