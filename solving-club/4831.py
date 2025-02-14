import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4831.txt'
sys.stdin = open(filename, 'r')

# 노선 수
T = int(input())

for t in range(1, T+1):
    # K,N,M
    K, N, M = map(int, input().split())
    # 충전기 있는 정류장
    unique_bus_stops = list(map(int, input().split()))
    # 전체 정류장
    bus_stops = [0]*(N+1)
    # 충전기 표시
    for i in range(M):
        bus_stops[unique_bus_stops[i]] += 1
    
    # 현재 버스의 위치
    bus = 0
    # 총 충전 횟수
    total_stops = 0
    
    while bus + K < N:
        # 버스가 최대로 갈 수 있는 길이부터 고려
        for i in range(bus+K, bus, -1):
            # 만약에 충전기가 있으면
            if bus_stops[i] == 1:
                # 버스 위치 변경해주고
                bus = i
                # 충전 횟수도 늘려주고
                total_stops += 1
                # for문 나오기 & 만약 버스가 종점을 안지나면 업데이트된 위치로 다시 for문 시작
                break
        # 충전기가 없었으면
        else:
            # 그냥 끝내기
            total_stops = 0
            break
            
    print(f'#{t} {total_stops}')
            