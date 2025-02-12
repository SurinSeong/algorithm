# 전기 버스
# 0 ~ N까지 이동, 한 번 충전으로 최대한 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호 주어짐
# 최소 몇 번 충전으로 충전해야할까?
# 충전 못하면 0
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4831.txt'
sys.stdin = open(filename, 'r')

# 노선 수
T = int(input())

for t in range(1, T+1):
    # 최대 이동 정류장 수, 마지막 정류장 번호, 충전기 설치 정류장 수
    K, N, M = map(int, input().split())
    # 정류장 번호 받기
    M_list = list(map(int, input().split()))
    # 총 정류장 리스트 만들기 (충전기 있는 것 체크하기)
    bus_stop = [0]*(N+1)
    
    for m in M_list:
        bus_stop[m] += 1
    
    # 버스의 위치 설정    
    bus_loc = 0
    # 충전 횟수
    charge = 0
    
    while bus_loc + K < N:
        for i in range(K+bus_loc, bus_loc, -1):
            # 충전기 있으면
            if bus_stop[i] == 1:
                # 위치 옮겨주기
                bus_loc = i
                # 충전 횟수 추가
                charge += 1
                # 다음 버스 위치로 이동
                break
        else:
            # 끝까지 못감
            charge = 0
            # while문 종료
            break
    
    print(f'#{t} {charge}')