import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23883.txt'
sys.stdin = open(filename, 'r')

# 이진 탐색
"""
저장된 값이 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브트리의 루트
완전 이진 트리로 만들기
루트의 번호는 1이다.
이진 탐색 트리의 루트에 저장된 값과 N//2 번 노드에 저장된 값은?
"""
def in_order(T):
    global cnt

    if T:
        in_order(left[T])
        cnt += 1
        nodes[T] = cnt
        in_order(right[T])



# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 마지막 자연수
    N = int(input())
    nodes = [0]*(N+1)
    left, right = [0]*(N+1), [0]*(N+1)
    answer = 0
    for i in range(1, N//2+1):
        l, r = i*2, i*2+1
        if l <= N:
            left[i] = l

        if r <= N:
            right[i] = r

    cnt = 0
    in_order(1)

    print(f'#{tc} {nodes[1]} {nodes[N//2]}')

