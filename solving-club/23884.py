import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23884.txt'
sys.stdin = open(filename, 'r')

# 사칙 연산
"""
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브트리의 결과와 오른족 서브트리의 결과에 해당 연산자를 적용한다.
"""
# 후위 연산
def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])

        if nodes[T] == '+':
            nodes[T] = nodes[left[T]] + nodes[right[T]]
        elif nodes[T] == '-':
            nodes[T] = nodes[left[T]] - nodes[right[T]]
        elif nodes[T] == '/':
            nodes[T] = nodes[left[T]] / nodes[right[T]]
        elif nodes[T] == '*':
            nodes[T] = nodes[left[T]] * nodes[right[T]]



# 테스트 케이스
T = 10

for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())
    nodes = [0]*(N+1)
    left, right = [0]*(N+1), [0]*(N+1)
    # 정점의 정보
    for _ in range(N):
        info = input().split()
        idx = int(info[0])
        if len(info) == 4:
            nodes[idx] = info[1]    # 연산자
            left[idx] = int(info[2])
            right[idx] = int(info[3])
        elif len(info) == 2:
            nodes[idx] = int(info[1])

    post_order(1)

    answer = int(nodes[1])

    print(f'#{tc} {answer}')