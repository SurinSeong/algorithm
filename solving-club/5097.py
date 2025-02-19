import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5097.txt'
sys.stdin = open(filename, 'r')

"""
회전
- N개의 숫자로 이루어진 수열
- 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번
- 수열의 맨 앞에 있는 숫자는?
"""
def change_front(rear, front, n):
    rear = (rear + 1) % n
    front = (front + 1) % n

    return rear, front


T = int(input())

for test_case in range(1, T+1):
    # 배열 원소의 개수, 회전 수
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    front, rear = 0, N-1    # 빈칸 및 마지막 원소 인덱스

    for _ in range(M):
        rear, front = change_front(rear, front, N)

    print(f'#{test_case} {array[front]}')



