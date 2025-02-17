import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_6485.txt'
sys.stdin = open(filename, 'r')

"""
[삼성시의 버스 노선]
- 5000개의 버스 정류장 (1 ~ 5000)
- 버스 노선은 N개
- i번쌔 버스 노선은 번호가 Ai ~ Bi인 모든 정류장만을 다니는 버스 노선
"""
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다닐까?


# 갈 수 있는 버스 정류장 체크
def available_bus_stop(arr, a, b):
    for i in range(a, b+1):
        arr[i] += 1

    return arr


# 각 정류장을 지나는 노선 수 체크
def check_lines(arr, n):
    cnt_list = [0]*n

    for i in range(n):
        cnt_list[i] = bus_stop[arr[i]]

    return cnt_list


# 테스트 케이스의 개수
T = int(input())

for test_case in range(1, T+1):
    # 버스 정류장
    bus_stop = [0]*5001
    # 버스 노선
    N = int(input())

    for _ in range(N):
        # 정류장
        A, B = map(int, input().split())

        bus_stop = available_bus_stop(bus_stop, A, B)    # 갈 수 있는 정류장 체크

    # 선택한 정류장 개수
    P = int(input())

    specific_stops = [0]*P
    for i in range(P):
        specific_stops[i] = int(input())

    bus_lines = check_lines(specific_stops, P)

    print(f'#{test_case} {" ".join([str(num) for num in bus_lines])}')