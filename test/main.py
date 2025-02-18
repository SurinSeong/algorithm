import sys

sys.stdin = open('Sample_input_2.txt', 'r')

"""
화분
N개의 화분 좌우로
2가지의 비료, 각각 담겨있음.

왼쪽 부터 비료를 준다.
한 화분에는 하나의 비료만. => 첫 번째 비료를 주었을 때 해당 화분의 식물이 자라는 높이와 두 번째 비료를 주었을 때 자라는 높이를 알고 있다
연속으로 같은 비료를 주면 원래 자라야할 높이보다 P만큼 덜 자람. 누적 안됨
전체 화분의 식물이 자라는 높이의 합이 가장 큰 경우 => 높이의 합 출력
"""
def change_continuous

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())    # N은 4 이상 20 이하
    pots = [0]*N    # 비료를 준 후 결과물 담을 리스트

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    # 모두 연속으로 안주는 경우
    for k in range(2):
        # first-second 순
        if k == 0:
            for i in range(N//2):
                pots[i*2], pots[i*2+1] = first[i*2], second[i*2+1]
            change1_total = sum(pots)
        else:
            for i in range(N//2):
                pots[i*2], pots[i*2+1] = second[i*2], first[i*2+1]
            change2_total = sum(pots)

    # 처음 기준 높이의 합
    max_total = max(change1_total, change2_total)

    # 마지막만 연속으로 주는 경우
    for k in range(2):
        # first-second 순
        if k == 0:
            for i in range(N//2):
                if i <= (N//2-1):
                    pots[i*2], pots[i*2+1] = first[i*2], second[i*2+1]
                    change1_total = sum(pots)
                else:


        else:
            for i in range(N//2):
                pots[i*2], pots[i*2+1] = second[i*2], first[i*2+1]
            change2_total = sum(pots)

    print(f'#{test_case} {max_total}')

# first = [4, 2, 6, 4]
#
# for i in range(1 << 4):    # 2의 4제곱
