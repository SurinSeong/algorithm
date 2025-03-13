"""
[당근 포장하기]
- 식당에 당근 공급

[식당 요구사항]
- N개의 당근을 주문하면 대, 중, 소로 구분해 포장
- 같은 크기의 당근은 같은 상자
- 비어 있을 수는 없음
- 한 상자에 N/2개를 초과하는 당근이 있어서는 안된다.
- 각 상자에 든 당근의 개수 차이가 최소
"""

# 총 수확 횟수
T = int(input())

for tc in range(1, T+1):
    # 당근 개수
    N = int(input())
    # 당근의 크기
    C = list(map(int, input().split()))
    # 상자
    boxes = [0] * 3
    
    answer = 0
    
    # 당근을 오름차순 정렬한다.
    for i in range(N-1):
        for j in range(i+1, N):
            if C[i] > C[j]:
                C[i], C[j] = C[j], C[i]
    
    
    print(f'#{tc} {answer}')