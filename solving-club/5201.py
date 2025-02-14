# 컨테이너 운반
# 컨테이너 개수 : N
# 트럭 개수 : M
# 트럭당 하나, 적재용량 있음
# 최대로 옮길 수 있는 무게는?
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5201.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 컨테이너 수, 트럭 수
    N, M = map(int, input().split())
    # 컨테이너 무게
    containers = list(map(int, input().split()))
    # 적재용량
    trucks = list(map(int, input().split()))
    # 운반 가능 최대 무게
    total = 0
    # 트럭 수가 없어질 때까지 while 문 돌리기
    while M > 0 and N > 0:
        big_truck = max(trucks)
        big_container = max(containers)
        if big_truck >= big_container:
            total += big_container
            trucks.remove(big_truck)
            containers.remove(big_container)
            M -= 1
            N -= 1
        else:
            containers.remove(big_container)
            N -= 1
            
    print(f'#{t} {total}')