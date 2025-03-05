import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23886.txt'
sys.stdin = open(filename, 'r')

# 노드의 합
"""
- 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어 있음.
- 루트 1번
- 같은 단계에서는 왼쪽에서 오른쪽으로 증가
- 단계가 꽉 차면 다음 단계의 왼쪽 부터 시작된다.
"""
# 후위 순회
def post_order(T):
    if T <= N:
        post_order(T*2)
        post_order(T*2+1)
        if heap[T] == 0:
            l, r = T*2, T*2+1
            if l <= N:
                heap[T] += heap[l]

            if r <= N:
                heap[T] += heap[r]



# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 힙
    heap = [0]*(N+1)
    # 관계성 보려고 좌우 자식 리스트 만들었음.
    # left, right = [0]*(N+1), [0]*(N+1)

    for _ in range(M):
        n, v = map(int, input().split())
        heap[n] = v
        # if n % 2:
        #     right[n//2] = n
        # else:
        #     left[n//2] = n

    post_order(1)

    answer = heap[L]

    print(f'#{tc} {answer}')