# 부분집합의 합
# 1 ~ 12을 원소로 가진 집합 A
# A의 부분 집합 중 N개의 원소를 가지고 있고, 원소의 합이 K인 부분집합의 개수 구하기
# 해당하는 부분집합이 없는 경우 0 출력
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4837.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # 부분집합 원소의 수, 부분 집합의 합
    N, K = map(int, input().split())
    # 결과
    result = 0
    # 집합 A
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for i in range(1 << 12): # 1<<12 : 부분집합의 개수
        elements = []
        for j in range(12): # 원소의 수만큼 비트를 비교한다.
            if i & (1 << j): # i의 j번 비트가 1인 경우
                elements.append(A[j])
        if (len(elements) == N) and (sum(elements) == K):
            result += 1
            
    print(f'#{t} {result}')
        