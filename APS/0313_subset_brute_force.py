"""
완전탐색으로 부분집합 구하기
- 세 명의 친구가 있다. {MIN, CO, TIM}
- 함께 영화관에 갈 수 있는 멤버를 구성하고자..

[구현 방법]
- Branch : 2개
- Level : 3개
"""
# p.9

arr = [0, 1]
path = []
name = ['MIN', 'CO', 'TIM']
N = len(name)

def print_name():
    print('{ ', end='')
    for i in range(N):
        if path[i]:
            print(name[i], end=' ')
    print('}')

def recur(cnt):
    if cnt == N:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        recur(cnt+1)
        path.pop()

recur(0)