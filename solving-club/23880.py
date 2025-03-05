import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23880.txt'
sys.stdin = open(filename, 'r')

# 중위 순회
def in_order(T):
    if T:
        in_order(left[T])
        print(nodes[T], end='')
        in_order(right[T])



# 10개의 테스트 케이스
T = 10

for tc in range(1, T+1):
    # 정점의 총 수
    N = int(input())
    # 정점 문자 알 수 있는 리스트
    nodes = [0]*(N+1)
    # 자식 노드를 담을 리스트
    left, right = [0]*(N+1), [0]*(N+1)
    for _ in range(N):
        info = input().split()
        idx = int(info[0])
        if len(info) == 4:
            nodes[idx] = info[1]
            left[idx] = int(info[2])
            right[idx] = int(info[3])

        elif len(info) == 3:
            nodes[idx] = info[1]
            left[idx] = int(info[2])

        elif len(info) == 2:
            nodes[idx] = info[1]

    print(f'#{tc}', end=' ')
    in_order(1)
    print()


