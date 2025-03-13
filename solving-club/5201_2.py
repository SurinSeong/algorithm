"""
[컨테이너 운반]
- 컨테이너 : N개
- 트럭 : M개
- A에서 B로 운반 (편도로 한번만)
- 트럭의 적재용량이 주어짐.
- 총 중량이 최대
"""
def move_containers():
    global W, T

    total = 0
    wi = 0

    for ti in range(M):
        while wi < N:
            if T[ti] >= W[wi]:    # 운반 가능하면
                total += W[wi]    # 화물 무게 추가
                wi += 1
                break

            # 운반 불가능하면
            wi += 1

    return total


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 컨테이너수, 트럭수
    N, M = map(int, input().split())
    # 화물 무게
    W = list(map(int, input().split()))
    # 적재용량
    T = list(map(int, input().split()))

    # 컨테이너 정렬하기
    for i in range(N-1):
        for j in range(i+1, N):
            if W[i] < W[j]:
                W[i], W[j] = W[j], W[i]

    # 트럭 정렬하기
    for i in range(M-1):
        for j in range(i+1, M):
            if T[i] < T[j]:
                T[i], T[j] = T[j], T[i]

    answer = move_containers()

    print(f'#{tc} {answer}')