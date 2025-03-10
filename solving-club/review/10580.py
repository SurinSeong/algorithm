"""
[전봇대]
- 세개 이상의 전선이 하나의 점에서 만나지 않는다.
- 총 교차점의 개수는?
"""

T = int(input())

for tc in range(1, T+1):
    # 전선 개수
    N = int(input())
    
    cables = []
    answer = 0
    
    for _ in range(N):
        A, B = map(int, input().split())
        for l, r in cables:
            if A < l and B > r:
                answer += 1
            
            if A > l and B < r:
                answer += 1
        
        cables.append([A, B])
        
    print(f'#{tc} {answer}')