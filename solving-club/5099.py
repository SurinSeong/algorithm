# import sys
# from pathlib import Path
#
# filename = Path.cwd() / 'solving-club/input/input_5099.txt'
# sys.stdin = open(filename, 'r')

"""
피자 굽기
- N개의 피자를 동시에 구울 수 있음.
- 치즈가 모두 녹으면 화덕에서 꺼낸다. (치즈의 양은 피자마다 다름)
- 1~M까지 M개의 피자를 순서대로 화덕에 넣음. 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내는 순서는 바뀔 수 있음.
- 가장 마지막 까지 남아있는 피자 번호는?

[규칙]
- 1번 위치에서 넣거나 뺄 수 있음.
- 화덕 내부의 피자 받침은 1번에서 잠시 꺼내 상태 확인 가능
- 치즈의 양 C -> 한 바퀴 돌고 꺼내면 C//2
- C가 0이되면 꺼내고 남은 피자 넣음
"""
def melting_cheese(arr):
    while 0 not in arr:
        arr = [c // 2 for c in arr]
    return arr


# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())
    # 피자에 있는 치즈의 개수
    C = list(map(int, input().split()))

    # 화덕
    fire = [-1]*N
    # 인덱스
    pizza = [0]*N
    # 다 녹은 치즈 피자
    result = []

    # 화덕에 피자 넣는다.
    for i in range(N):
        fire[i] = C[i]
        pizza[i] = i+1

    # 남은 피자 개수 만큼 반복
    for i in range(M-N):
        fire = melting_cheese(fire)    # 치즈 녹이기
        for j in range(N-1):    # 0인 자리 찾기
            if fire[i] == 0:
                result.append(pizza[i])
                pizza[i] = N+i
                fire[i] = C[N+i]

    print(fire)






    print(f'#{test_case} {result}')