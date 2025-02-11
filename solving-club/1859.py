# 백만장자 프로젝트
# 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음.
# 하루에 최대 1만큼 구입 가능
# 판매는 얼마든지 가능

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 연속된 N일
    N = int(input())
    # 매매가
    priority = list(map(int, input().split()))
    
    # 앞에서부터 비교하면서 진행해보기
    for i in range(1, N):
        # 현재의 값이 이전의 값보다 크거나 같으면
        if priority[i-1] <= priority[i]:
            # 가장 큰 값 설정해주고 넘어가기
            max_idx = i
        # 현재의 값이 이전의 값보다 작으면
        else:
            previous_max_idx = max_idx
            max_idx = i-1
            
            
            