import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_23885.txt'
sys.stdin = open(filename, 'r')

# 이진 힙
"""
[특징]
- 항상 완전 이진 트리를 유지 하기 위해 '마지막 노드 뒤에 새 노드를 추가'한다.
- 부모 노드의 값 < 자식 노드의 값

- 1000000 이하인 N개의 서로 다른 자연수
- 순서대로 이진 최소 힙에 저장한다.
- 조상 노드에 저장된 정수의 합은?
"""
# 삽입
def enq(n):
    global last    # 마지막 정점

    last += 1
    heap[last] = n    # 삽입

    c = last
    p = last // 2

    # 부모가 아직 있고, 아직 바꿀게 남아있으면
    while p != 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]    # 자리 바꿔주기

        c = p    # 부모 노드 번호를 바꿀 노드 번호로 바꿔주고
        p = c // 2    # 바꿀 노드 번호의 부모 노드 번호를 찾아준다.


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 자연수 개수
    N = int(input())
    # 자연수들
    number_list = list(map(int, input().split()))
    # 자식을 인덱스로 부모를 저장한다.
    heap = [0]*(N+1)

    last = 0
    for num in number_list:
        enq(num)

    answer = 0

    last = N // 2

    while last != 0:
        answer += heap[last]
        last //= 2

    print(f'#{tc} {answer}')







