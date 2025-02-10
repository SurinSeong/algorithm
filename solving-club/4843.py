import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4843.txt'
sys.stdin = open(filename, 'r')


# 특별한 정렬
def special_sort(arr, n):
    # 홀짝으로 나눠서 하기
    # 만약 인덱스가 짝수면 -> max / 홀수면 -> min
    for i in range(10):
        target_idx = i
        for j in range(i+1, n):
            if i % 2 == 0:
                # max 찾기
                if arr[target_idx] < arr[j]:
                    target_idx = j
            else:
                if arr[target_idx] > arr[j]:
                    target_idx = j

        arr[i], arr[target_idx] = arr[target_idx], arr[i]

    return arr[:10]


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # 정수의 개수
    N = int(input())
    # N개의 정수
    number_list = list(map(int, input().split()))

    print(f'#{t}', end=' ')

    for num in special_sort(number_list, N):
        print(num, end=' ')

    print()
