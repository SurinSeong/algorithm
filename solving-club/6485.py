# 삼성시에 있는 5000개의 버스 정류장
# N : 버스 노선
# i번째 버스 노선 : Ai <= 정류장 번호 <= Bi

# 테스트 케이스 수
T = int(input())

# T번 반복
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    # 정류장 5000개에 대한 리스트 만들기
    bus_stop = [0]*5001    # 정류장: 1 ~ 5000
    # 버스 노선 개수
    N = int(input())
    # 버스 노선 마다 갈 수 있는 정류장 찾기
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_stop[i] += 1

    # P 받기
    P = int(input())
    for _ in range(P):
        # p번 반복
        C = int(input())
        if _ == P-1:
            print(bus_stop[C])
        else:
            print(bus_stop[C], end=' ')