import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23882.txt'
sys.stdin = open(filename, 'r')

# 서브 트리
"""
노드 N을 루트로 하는 서브 트리에 속한 노드의 개수는?

[트리 조건]
- 부모 자식 사이에 특별한 규칙 없음
- 부모가 없는 노드가 전체의 루트 노드가 된다.
"""
def count_nodes(T):
    global cnt

    if T:
        cnt += 1
        count_nodes(left[T])
        count_nodes(right[T])


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 간선의 개수, N
    E, N = map(int, input().split())
    # 노드쌍
    pairs = list(map(int, input().split()))
    # 부모 노드에 대응되는 왼, 오 자식 노드 리스트
    left, right = [0]*(E+2), [0]*(E+2)
    for i in range(E):
        p, c = pairs[i*2], pairs[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    count_nodes(N)

    print(f'#{tc} {cnt}')